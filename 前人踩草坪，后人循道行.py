from Crypto.Util.number import *
from random import randrange
import gmpy2
from origination import flag
#提示：flag = b'EVA{..........}'
q = getPrime(12)

for i in range(q+1, pow(2, 12)):
    if gmpy2.is_prime(i):
        p = i
        break
k = [randrange(1,q) for i in range(2)]
h = [randrange(1,q) for i in range(2)]
for i in range(len(flag)):
    footprint = flag[i]
    for j in range(2):
        k[j] = footprint = footprint * k[j] % p
        h[j] = footprint = footprint * h[j] % q
    print(str(footprint)+',')


#output:193,928,1675,61,2053,1717,1519,87,1634,726,1302,885,1646,515,791,234,614,2325,898,1761,1997,1153,316,