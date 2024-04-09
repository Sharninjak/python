import base64


def decode_base64_file(encoded_file_path, output_file_path):
    try:
        # 打开被编码的文件并读取内容
        with open(encoded_file_path, 'rb') as encoded_file:
            encoded_data = encoded_file.read()

        # 解码 Base64 数据
        decoded_data = base64.b64decode(encoded_data)

        # 将解码后的数据写入新文件
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decoded_data)

        print(f"解码成功，已保存到 {output_file_path}")
    except Exception as e:
        print(f"解码失败：{e}")


def decode_from_txt():
    # 替换成你的被编码文件的路径和输出文件的路径
    encoded_file_path = 'task.txt'
    output_file_path = 'task_output.png'

    # 调用解码函数
    decode_base64_file(encoded_file_path, output_file_path)


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # 读取图像文件的二进制数据
        image_binary = image_file.read()

        # 进行Base64编码
        base64_encoded = base64.b64encode(image_binary).decode('utf-8')

    return base64_encoded


def write_base64_to_file(base64_data, output_file):
    with open(output_file, "w") as output:
        output.write(base64_data)


def encode_to_txt():
    # 图片文件的路径
    image_path = "task_output.png"

    # 调用函数进行编码
    base64_data = encode_image_to_base64(image_path)

    # 将Base64数据写入文件
    output_file_path = "task_output_output.txt"
    write_base64_to_file(base64_data, output_file_path)

    # 打印输出文件的路径
    print("Base64数据已写入文件:", output_file_path)


def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            # 大写字母解密
            if char.isupper():
                result += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            # 小写字母解密
            else:
                result += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            result += char
    return result


def run_caesar_decrypt():
    decoded_text = "..."  # 用解码后的文本替换这里的"..."
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(decoded_text, shift)
        print(f"Shift {shift}: {decrypted_text}")


def gbk_to_2():
    # 输入文件名和输出文件名
    input_file_name = 'task.txt'
    output_file_name = 'task_to_2.txt'

    # 以GBK编码方式读取文本文件
    with open(input_file_name, 'r', encoding='gbk') as input_file:
        text_content = input_file.read()

    # 将文本内容转换为二进制数据
    binary_data = text_content.encode('gbk')

    # 将二进制数据写入输出文件
    with open(output_file_name, 'wb') as output_file:
        output_file.write(binary_data)

    print(f"已将GBK编码的文本文件转换为二进制文件：{output_file_name}")


def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.read()
        content2 = f2.read()
        differences=[]
        # 找到不同的字节
        # differences = [(i, content1[i], content2[i]) for i in range(min(len(content1), len(content2))) if content1[i] != content2[i]]
        j = 0
        for i in range(min(len(content1), len(content2))):
            if content1[i+j] != content2[i]:
                differences.append((i + j, content1[i + j], content2[i]))
                j += 1
        return differences


def find_different():
    file1_path = 'task.txt'
    file2_path = 'task_output_output.txt'
    #
    # with open(file1_path, 'rb') as f1, open(file2_path, 'rb') as f2:
    #     t1 = bytearray(f1.read())
    #     t2 = bytearray(f2.read())
    # while t1 != b'':
    #     if t1[0] == t2[0]:
    #         t1.pop(0)
    #         t2.pop(0)
    #     if t1[0] != t2[0]:
    #         print(t2[0], end=",")
    #         t2.pop(0)
    differences = compare_files(file1_path, file2_path)

    needtoflag = []
    if differences:
        print("发现不同的字节：")
        for i in range(len(differences)):
            print(differences[i])
            needtoflag.append(differences[i][1])
    else:
        print("两个文件相同。")
    # for i in range(len(differences)):
    #     print()
    print(needtoflag)
    return needtoflag


def test():
    file1 = 'task.txt'
    # file1 = 'task_output_output.txt'
    with open(file1, 'rb') as f1:
        content1 = f1.read()
        # for i in range(len(content1)):
        #     print(content1[i])
        for i in range(600):
            print(i, content1[i], '  ', chr(content1[i]))


def difference_to_flag(need_to_flag):
    # numbers = [182, 188, 177, 183, 203, 163, 128, 189, 131, 196, 129, 189, 181, 195, 175, 199, 181, 175, 189, 197, 133,
    #            196, 175, 195, 181, 181, 187, 175, 132, 190, 195, 199, 181, 194, 195, 175, 129, 190, 175, 196, 184, 181,
    #            175, 148, 177, 194, 187, 190, 181, 195, 195, 205]
    numbers = need_to_flag
    # Subtract 80 from each number and convert to characters
    result = ''.join(chr(num - 80) for num in numbers)

    print(result)


def __main__():
    decode_from_txt()
    encode_to_txt()
    # run_caesar_decrypt()
    # gbk_to_2()
    find_different()
    # test()
    difference_to_flag(find_different())


__main__()

