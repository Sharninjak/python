from RSA import CPA, RSAENCODE

rsa = RSAENCODE()
rsa.rsa_decode(r'.\key_encode.bin', r'key.bin')
# 使用上述函数进行解密
cpa = CPA()
cpa.decrypt_image(r'.\RSA_encode.png', r'.\RSA_decode.png')
