import secrets
import uuid

print(uuid.uuid4())

password = secrets.token_hex(20)  # 返回十六进制随机文本字符串。字符串有20个随机字节
print("token_hex:", password)
password = secrets.token_bytes(20)  # 返回含20个字节的随机字节字符串
print("token_bytes:", password)
password = secrets.token_urlsafe(20)  # 返回安全的 URL 随机文本字符串，包含20个随机字节
print("token_urlsafe:", password)
# def generate_password(length=12):
#     alphabet = string.ascii_letters + string.digits + string.punctuation
#     password1 = ''.join(secrets.choice(alphabet) for _ in range(length))
#     return password1
