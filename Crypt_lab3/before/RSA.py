from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from PIL import Image
import numpy as np
import Crypto.PublicKey.RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
import base64
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


# 封装为一个class，这样可以抽象的调用加密解密接口，而且可以封装一个oracle
class RSA(object):
    # 初始 决定好秘钥和iv
    def __init__(self, key_path=r".\key.bin", iv_path=r".\iv.bin", private_key_path=r".\private_key.pem",
                 public_key_path=r".\public_key.pem"):
        # 生成或读取密钥和IV
        if not os.path.exists(key_path) or not os.path.exists(iv_path) or not os.path.exists(public_key_path)\
                or not os.path.exists(private_key_path):
            x = Random.new().read
            print(x)
            y = Crypto.PublicKey.RSA.generate(2048, Random.new().read)
            self.private_key = y.exportKey()  # 生成私钥
            self.public_key = y.publickey().exportKey()  # 生成公钥
            public_key_rsakey = y.public_key()
            self.key = os.urandom(32)  # AES-256要求的密钥长度
            self.iv = os.urandom(16)   # OFB模式的IV大小
            print(type(self.public_key))
            self.cipher = Cipher(algorithms.AES(self.key), modes.OFB(self.iv), backend=default_backend())
            # 对key用public_key加密 保存几个密钥和初始化向量
            cipher = PKCS1_cipher.new(public_key_rsakey)
            encrypt_key = base64.b64encode(cipher.encrypt(self.key))
            print(type(self.public_key))
            with open(key_path, "wb") as key_file:
                key_file.write(encrypt_key)
            with open(iv_path, "wb") as iv_file:
                iv_file.write(self.iv)
            with open(public_key_path, "wb") as public_key_file:
                public_key_file.write(self.public_key)
            with open(private_key_path, "wb") as private_key_file:
                private_key_file.write(self.private_key)
        else:
            with open(key_path, "rb") as key_file:
                self.key = key_file.read()
            with open(iv_path, "rb") as iv_file:
                self.iv = iv_file.read()
            with open(public_key_path, "rb") as public_key_file:
                self.public_key = public_key_file.read()
            with open(private_key_path, "rb") as private_key_file:
                self.private_key = private_key_file.read()

            self.cipher = Cipher(algorithms.AES(self.key), modes.OFB(self.iv), backend=default_backend())

    # 加密路线
    def encrypt_schema(self, plaintext):
        encryptor = self.cipher.encryptor()
        # update负责处理大部分的密文数据 finalize处理可能的最后一个数据块 标志着解密操作的结束
        encrypted_data = encryptor.update(plaintext) + encryptor.finalize()

        return encrypted_data

    # 解密路线
    def decrypt_schema(self, encode):
        decryptor = self.cipher.decryptor()
        plaintext = decryptor.update(encode) + decryptor.finalize()

        return plaintext

    def process_image(self, input_path, output_path, mode='encrypt'):
        with Image.open(input_path) as img:
            r, g, b = img.split()
        print(type(r))
        # 按照 r g b 通道对图片分别进行加解密
        if mode == 'encrypt':  # 加密
            # 接受一个表示图像数据的字节串作为输入，然后使用已经初始化的加密器（self.cipher.encryptor()）
            # 对该数据进行加密处理，并返回加密后的字节串。
            r_processed = self.encrypt_schema(np.array(r, dtype=np.uint8).tobytes())
            g_processed = self.encrypt_schema(np.array(g, dtype=np.uint8).tobytes())
            b_processed = self.encrypt_schema(np.array(b, dtype=np.uint8).tobytes())
        else:  # 解密
            cipher = PKCS1_cipher.new(self.private_key)
            back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)
            r_processed = self.decrypt_schema(np.array(r, dtype=np.uint8).tobytes())
            g_processed = self.decrypt_schema(np.array(g, dtype=np.uint8).tobytes())
            b_processed = self.decrypt_schema(np.array(b, dtype=np.uint8).tobytes())
        # print(bin(int.from_bytes(r_processed, 'big'))[2:].zfill(8))
        # 重建图像
        # L表示灰度图像，即图像只有一个通道，对三个通道分别处理
        r_new = Image.frombytes('L', r.size, r_processed)
        g_new = Image.frombytes('L', g.size, g_processed)
        b_new = Image.frombytes('L', b.size, b_processed)
        img_new = Image.merge("RGB", (r_new, g_new, b_new))
        img_new.save(output_path)

    def encrypt_image(self, input_path, output_path):
        self.process_image(input_path, output_path, mode='encrypt')

    def decrypt_image(self, input_path, output_path):
        self.process_image(input_path, output_path, mode='decrypt')
