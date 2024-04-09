from Crypto.PublicKey import RSA
from Crypto.Util.number import GCD
from Crypto.Util.number import inverse
from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import numpy as np
import os
from Crypto.Cipher import PKCS1_OAEP
import base64
#  算法由两个密钥，即公钥和私钥组成。
# 准备两个非常大的素数p和q
# 利用字符串模拟计算大素数p和q的乘积n=pq
# m=(p-1)(q-1) m为n的欧拉函数
# 找到一个数e(1<e<m)满足e和m互素）
# 计算e在模m域上的逆元d 即满足ed mod m =1
#  (n,e)为公钥 (n,d)为私钥


def calculate_private_exponent(p, q, e):
    phi_n = (p - 1) * (q - 1)
    # 计算模逆元
    d = inverse(e, phi_n)
    return d


def decrypt_rsa(file_path, private_key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
        cipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher_rsa.decrypt(encrypted_data)
    return decrypted_data


def decrypt_pixels(encrypted_pixels, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_pixels = decryptor.update(encrypted_pixels) + decryptor.finalize()
    return decrypted_pixels


def decrypt_image(encrypted_image_path, decrypted_image_path, key, iv):
    # 打开加密后的图像
    with open(encrypted_image_path, 'rb') as f:
        ciphertext = f.read()
        padding_length = ciphertext[-1]
        ciphertext = ciphertext[:-padding_length]
    with Image.open(encrypted_image_path) as img:
        rgba_img = img.convert('RGBA')
        # 将图像数据转换为一维byte数组
        pixels = np.array(rgba_img)
        pixels_bytes = pixels.tobytes()
        # 解密像素数据
        decrypted_pixels_bytes = decrypt_pixels(pixels_bytes, key, iv)

        # 将解密的像素数据转换回图像格式
        decrypted_pixels = np.frombuffer(decrypted_pixels_bytes, dtype=np.uint8).reshape(pixels.shape)
        decrypted_img = Image.fromarray(decrypted_pixels, 'RGBA')

        # 保存解密后的图像
        decrypted_img.save(decrypted_image_path)


def rsa_common_factor():
    key1_path = r'.\key1.pem'
    key2_path = r'.\key2.pem'
    # 读取公钥1
    with open(key1_path, 'r') as f:
        public_key1 = RSA.importKey(f.read())

    # 读取公钥2
    with open(key2_path, 'r') as f:
        public_key2 = RSA.importKey(f.read())

    # 获取两个公钥的模数n
    n1 = public_key1.n
    n2 = public_key2.n
    print("n1:", n1)
    print("n2:", n2)
    # 计算两个模数的公共因子q
    q = GCD(n1, n2)
    print("Common factor q:", q)
    # 选取的与m互质的数e
    e1 = public_key1.e
    e2 = public_key2.e
    # e1==e2
    print("e1", e1)
    print("e2", e2)
    p1 = n1 // q
    p2 = n2 // q
    print(p1, p2)
    print("Common factor q:", q)
    # 已知的 p1、q 和 e1 计算私钥指数d1
    d1 = calculate_private_exponent(p1, q, e1)
    print("d1:", d1)
    rsa_key = RSA.construct((n1, e1, d1, p1, q))
    print("rsa_key1:", rsa_key)
    dec_key_base64 = decrypt_rsa('sym_key.enc', rsa_key)
    print("dec_key_base64:", dec_key_base64)
    dec_key = base64.b64decode(dec_key_base64)
    print("dec_key:", dec_key)
    key = dec_key[:16]  # 128位对称密钥,16字节
    iv = dec_key[16:]  # IV
    print("key:", key)
    print("iv:", iv)
    encrypted_image = 'enc1.png'
    decrypted_image_path = os.path.join('rsa_common_factor_decode.png')
    decrypt_image(encrypted_image, decrypted_image_path, key, iv)


if __name__ == "__main__":
    rsa_common_factor()
