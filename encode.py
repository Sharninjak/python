# hex_string = "676f666e84413d3f4676474e504881558354525b5e625d5c6a6c6c6d669d7570a673aa797b7c7f84b5d0"
# byte_data = bytes.fromhex(hex_string)
#
# try:
#     decoded_text = byte_data.decode("latin-1")
#     print("UTF-8 Decoded:", decoded_text)
# except UnicodeDecodeError as e:
#     print("UTF-8 Decoding Error:", e)
#
# # You can try other common encodings such as "latin-1", "utf-16", etc.

# import base64
#
# base64_string = "676f666e84413d3f4676474e504881558354525b5e625d5c6a6c6c6d669d7570a673aa797b7c7f84b5d0"
# byte_data = base64.b64decode(base64_string)
#
# try:
#     # decoded_text = byte_data.decode("utf-8")
#     print("Base64 Decoded:", byte_data)
# except UnicodeDecodeError as e:
#     print("UTF-8 Decoding Error:", e)
import binascii


def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str.encode())
    return ascii_str


hex_input = '67 6f 66 6e 84 41 3d 3f 46 76 47 4e 50 48 81 55 83 54 52 5b 5e 62 5d 5c 6a 6c 6c 6d 66 9d 75 70 a6 73 aa 79 7b 7c 7f 84 b5 d0'
ascii_output = hex_to_ascii(hex_input)
print('ascii result is:{0}'.format(ascii_output))

# 将十六进制字符串转换为整数列表
hex_values = [int(x, 16) for x in hex_input.split()]
print(hex_values)
result = ''
for i in range(len(hex_values)):
    result = result + (chr(hex_values[i] - 2 * (i + 1) + 1))

print(result)

