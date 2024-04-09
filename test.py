from Crypto.Random import get_random_bytes


def generate_key():
    a = get_random_bytes(16)
    print(a)
    return a  # AES-128


def read_bin():
    with open('iv.bin', 'rb') as f:
        byte = f.read(1)
        while byte:
            byte_str = bin(int.from_bytes(byte, 'big'))[2:].zfill(8)  # 将每个字节转换为 01 串
            print(byte_str, end=' ')
            byte = f.read(1)


if __name__ == '__main__':
    # generate_key()
    read_bin()
