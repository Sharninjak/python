from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# 生成RSA密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# 将公钥和私钥序列化为PEM格式
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# 加载公钥和私钥
private_key = serialization.load_pem_private_key(private_key_pem, password=None)
public_key = serialization.load_pem_public_key(public_key_pem)

# 生成对称密钥
symmetric_key = os.urandom(32)  # 256位的对称密钥

# 使用公钥加密对称密钥
encrypted_symmetric_key = public_key.encrypt(
    symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 使用对称密钥加密图片
image_path = 'example.jpg'
with open(image_path, 'rb') as f:
    plaintext = f.read()

iv = os.urandom(16)  # 生成随机IV
cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# 使用私钥解密对称密钥
decrypted_symmetric_key = private_key.decrypt(
    encrypted_symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 使用对称密钥解密图片
cipher = Cipher(algorithms.AES(decrypted_symmetric_key), modes.CFB(iv))
decryptor = cipher.decryptor()
decrypted_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# 将解密后的图片保存到文件中
decrypted_image_path = 'decrypted_image.jpg'
with open(decrypted_image_path, 'wb') as f:
    f.write(decrypted_plaintext)
