import random
import os


# write file
def write_txt(name1, content):
    path1 = os.getcwd() + '\\' + name1 + '.txt'
    with open(path1, 'w', encoding='utf8') as f:  # 写入新文件
        for i in content:
            f.write(i)
        f.close()


# read file
def read_txt(name2):
    content = []
    length = 0
    with open(name2, "r", encoding='utf8') as f:
        for i in f.readlines():
            i = i.rstrip("\t\n").lstrip("\t\n")
            content.append(i)
            length += len(i)
    f.close()
    return content, length


# Unicode数据编码为二进制
def to_two(content):
    content_two = []
    for i in content:
        n = []
        for j in i:
            # ord():character->unicode  bin():integer->binary
            j = bin(ord(j)).replace('0b', '')
            n.append(j)
        content_two.append(n)
    return content_two


# 二进制还原成unicode数据
def two_return(content_two):
    content_return = []
    for i in content_two:
        n = ''
        for j in i:
            j = ''.join([chr(i) for i in [int(j, 2)]])
            n += j
        content_return.append(n)
    return content_return


# def pro_secretkey(plaintext1):
#     plaintext_two = to_two(plaintext1)
#     # print("plaintext_two:", plaintext_two)
#     secretkey1 = []
#
#     for i in plaintext_two:
#         tip = []
#         for j in i:
#             key = ''
#             # 密钥生成在4-15位随意生成
#             for l in range(random.randint(4, 15)):
#                 key += str(random.randint(0, 1))
#                 # print("key:", key)
#
#             # 密钥碎片（总密钥一部分）如果0开头
#             if key.startswith('0'):  # 开头如果为0，往前添置一个1
#                 key = '1' + key
#                 num = random.randint(2, len(key) - 1)
#                 key = key[:num] + key[num + 1:]  # 随机删除一个数字
#
#             # 密钥碎片中包含'\','\n','\r'，随机删除碎片一位数字
#             #                             并在末尾加11（也是防止出现上述情况）
#             if key == '1011100' or key == '1010' or key == '1101':
#                 num = random.randint(2, len(key))
#                 key = key[:num] + key[num + 1:]  # 随机删除一个数字
#                 key += '11'
#             tip.append(key)
#         secretkey1.append(tip)
#
#         # 记录密钥
#
#     write_txt('OPT_secretkey', two_return(secretkey1))
#
#     return two_return(secretkey1)

def pro_secretkey(length):
    # 生成随机的01串
    key = ''.join(random.choice('01') for _ in range(8 * length))
    # 将01串转换为ASCII码并写入文件
    ascii_key = ''.join(chr(int(key[i:i + 8], 2)) for i in range(0, len(key), 8))
    # print("ascii_key={}".format(ascii_key))
    with open('OPT_secretkey.txt', 'w', encoding='utf-8') as f:
        f.write(ascii_key)
    return ascii_key


def xor_process(key, plain):
    key_binary = to_two(key)
    plain_binary = to_two(plain)

    # 进行异或
    text_return = []
    for i in range(len(key_binary)):
        tip = []
        for j in range(len(key_binary[i])):
            #  结果为字符串形式
            k = bin(int(key_binary[i][j], 2) ^ int(plain_binary[i][j], 2))[2:]
            tip.append(k)
        text_return.append(tip)
    # 返回异或后的内容
    result1 = two_return(text_return)
    result1 = ''.join(result1)
    return result1


if __name__ == "__main__":
    # read plaintext
    name = 'OPT_plaintext'
    path = os.getcwd() + "\\" + name + ".txt"
    plaintext, plaintext_len = read_txt(path)
    plaintext = str(plaintext[0])
    print("PLAINTEXT:", plaintext, "\n")
    # create key
    secretkey = pro_secretkey(plaintext_len)
    print("SECRETKEY:", secretkey, "\n")
    # create ciphertext
    ciphertext = xor_process(secretkey, plaintext)
    print('CIPHERTEXT:{}\n'.format(ciphertext))
    # write ciphertext
    write_txt('OPT_ciphertext', ciphertext)
    # decode
    plaintext_new = xor_process(secretkey, ciphertext)
    print('AFTER DECODING:', plaintext_new)
    name_decode = 'OPT_decode'
    path1 = os.getcwd() + '\\' + name_decode + '.txt'
    with open(path1, 'w', encoding='utf8') as f:  # 写入新文件
        for i in plaintext_new:
            f.write(i + '\n')
        f.close()
