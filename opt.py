import random
import os


# write file
def write_txt(name1, content):
    path1 = os.getcwd() + '\\' + name1 + '.txt'
    with open(path1, 'w', encoding='utf8') as f:  # 写入新文件
        for i in content:
            f.write(i + '\n')


# read file
def read_txt(name2):
    content = []
    with open(name2, "r", encoding='utf8') as f:
        for i in f.readlines():
            content.append(i.strip())
    return content


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
            j = ''.join([chr(int(j, 2))])
            n += j
        content_return.append(n)
    return content_return


def pro_secretkey(plaintext1):
    plaintext_two = to_two(plaintext1)
    secretkey1 = []

    for i in plaintext_two:
        tip = []
        for j in i:
            key = ''
            # 密钥生成在4-15位随意生成
            for l in range(random.randint(4, 15)):
                key += str(random.randint(0, 1))
                # print("key:", key)

            # 密钥碎片（总密钥一部分）如果0开头
            if key.startswith('0'):  # 开头如果为0，往前添置一个1
                key = '1' + key
                num = random.randint(2, len(key) - 1)
                key = key[:num] + key[num + 1:]  # 随机删除一个数字

            # 密钥碎片中包含'\','\n','\r'，随机删除碎片一位数字
            #                             并在末尾加11（也是防止出现上述情况）
            if key == '1011100' or key == '1010' or key == '1101':
                num = random.randint(2, len(key))
                key = key[:num] + key[num + 1:]  # 随机删除一个数字
                key += '11'
            tip.append(key)
        secretkey1.append(tip)

    write_txt('OPT_secretkey', two_return(secretkey1))

    return two_return(secretkey1)


def xor_process(reference, change):
    # 内容变为二进制数据
    reference_two = to_two(reference)
    change_two = to_two(change)

    # 进行异或
    text_return = []
    for i in range(len(reference_two)):
        tip = []
        for j in range(len(reference_two[i])):
            # ^ 需要数据位int（10进制）类型
            #  结果为字符串形式
            k = bin(int(reference_two[i][j], 2) ^ int(change_two[i][j], 2))[2:]
            tip.append(k)
        text_return.append(tip)

    # 返回异或后的内容
    return two_return(text_return)


if __name__ == "__main__":
    # 读取明文
    name = 'OPT_plaintext'
    path = os.getcwd() + "\\" + name + ".txt"
    plaintext = read_txt(path)
    # 密钥生成
    secretkey = pro_secretkey(plaintext)
    # 密文生成
    ciphertext = xor_process(secretkey, plaintext)
    print('ciphertext:', ciphertext)
    # 密文记录
    write_txt('OPT_ciphertext', ciphertext)
    # 解密
    plaintext_new = xor_process(secretkey, ciphertext)
    print('解密后：', plaintext_new)
