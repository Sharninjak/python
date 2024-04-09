from RSA import CPA, RSAENCODE


rsa = RSAENCODE()
rsa.rsa_encode(r'.\key.bin', r'.\key_encode.bin')
cpa = CPA()
cpa.encrypt_image(r'.\RSA_origin.png', r'.\RSA_encode.png')
