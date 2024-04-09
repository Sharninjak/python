from Crypto.Util.number import *
from random import randrange
import gmpy2


# from origination import flag
# 提示：flag = b'EVA{..........}'
def task():
    q = getPrime(12) # q < 4096
    flag = b'1'

    for i in range(q+1, pow(2, 12)):
        if gmpy2.is_prime(i):
            p = i
            break
    k = [randrange(1,q) for i in range(2)]
    # 创建了一个包含两个元素的列表 k，其中每个元素都是在范围 [1, q) 内随机选择的整数。
    # randrange(1, q) 用于生成一个范围在1到q-1之间（包括1但不包括q）的随机整数。
    h = [randrange(1,q) for i in range(2)]
    print(q)
    print(p)
    print(k)
    print(h)
    for i in range(len(flag)):
        footprint = flag[i]
        print("footprint", footprint)
        for j in range(2):
            k[j] = footprint * k[j] % p
            footprint = footprint * k[j] % p
            h[j] = footprint * h[j] % q
            footprint = footprint * h[j] % q
        print(str(footprint)+',')
    print(k)
    print(h)
    # print(49*1499%p)


def get_prime():
    j = 0
    for i in range(4100):
        if gmpy2.is_prime(i):
            j += 1
            print(i)
    print("total:",j)


def __main__():
    # task()
    get_prime()


__main__()


#output:193,928,1675,61,2053,1717,1519,87,1634,726,1302,885,1646,515,791,234,614,2325,898,1761,1997,1153,316,
