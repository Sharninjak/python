from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from os import urandom

# Key and Initialization Vector generation
key = urandom(16)  # Generate a random 16-byte key
iv = urandom(8)    # Generate a random 8-byte IV (Initialization Vector)

# Creating a Blowfish cipher object
cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=default_backend())

# Prepare data for encryption (with padding)
data = b"Secret Message"
padder = padding.PKCS7(64).padder()  # 64 bit (8 byte) padding for Blowfish
padded_data = padder.update(data) + padder.finalize()

# Encrypting data
encryptor = cipher.encryptor()
encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

print(f"ENCRYPTED DATA IS: {encrypted_data}")

# Decrypting data
decryptor = cipher.decryptor()
decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

# Remove padding after decryption
unpadder = padding.PKCS7(64).unpadder()
decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

print(f"DECRYPTED DATA IS: {decrypted_data}")

#output
#ENCRYPTED DATA IS: b'\xc4\xf6\xad\xa3n\xc6\xc3W\xb9\xcb,=\xf1\xd9\xaa\xa6'
#DECRYPTED DATA IS: b'Secret Message'