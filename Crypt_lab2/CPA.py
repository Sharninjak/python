from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from PIL import Image
import numpy as np


# 封装为一个class，这样可以抽象的调用加密解密接口，而且可以封装一个oracle
class CPA(object):
    # 初始 决定好秘钥和iv
    def __init__(self, key_path=r".\key.bin", iv_path=r".\iv.bin"):
        # 生成或读取密钥和IV
        if not os.path.exists(key_path) or not os.path.exists(iv_path):
            self.key = os.urandom(32)  # AES-256要求的密钥长度
            self.iv = os.urandom(16)   # OFB模式的IV大小
            print(len(self.key))
            with open(key_path, "wb") as key_file:
                key_file.write(self.key)
            with open(iv_path, "wb") as iv_file:
                iv_file.write(self.iv)
            self.cipher = Cipher(algorithms.AES(self.key), modes.OFB(self.iv), backend=default_backend())
        else:
            with open(key_path, "rb") as key_file:
                self.key = key_file.read()
            with open(iv_path, "rb") as iv_file:
                self.iv = iv_file.read()
            print(len(self.key))
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
        print(r)
        # 按照 r g b 通道对图片分别进行加解密
        if mode == 'encrypt':  # 加密
            # 接受一个表示图像数据的字节串作为输入，然后使用已经初始化的加密器（self.cipher.encryptor()）
            # 对该数据进行加密处理，并返回加密后的字节串。
            r_processed = self.encrypt_schema(np.array(r, dtype=np.uint8).tobytes())
            g_processed = self.encrypt_schema(np.array(g, dtype=np.uint8).tobytes())
            b_processed = self.encrypt_schema(np.array(b, dtype=np.uint8).tobytes())
        elif mode == 'decrypt':  # 解密
            r_processed = self.decrypt_schema(np.array(r, dtype=np.uint8).tobytes())
            g_processed = self.decrypt_schema(np.array(g, dtype=np.uint8).tobytes())
            b_processed = self.decrypt_schema(np.array(b, dtype=np.uint8).tobytes())
        else:
            r_array = np.array(r, dtype=np.uint8)
            g_array = np.array(g, dtype=np.uint8)
            b_array = np.array(b, dtype=np.uint8)
            height = r_array.shape[0]
            tamper_height = height // 2
            r_array[:tamper_height] ^= 0xFF
            g_array[:tamper_height] ^= 0xFF
            b_array[:tamper_height] ^= 0xFF
            r_processed = self.decrypt_schema(r_array.tobytes())
            g_processed = self.decrypt_schema(g_array.tobytes())
            b_processed = self.decrypt_schema(b_array.tobytes())

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

    def cca_attack_image(self, input_path, output_path):
        self.process_image(input_path, output_path, mode='attack')
