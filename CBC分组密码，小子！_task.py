import random
import base64

def string2binary(str):
  result = []
  for i in range(0, len(str), 2):
    binary = ""
    for char in str[i:i+2]:
      binary += bin(ord(char))[2:].zfill(8)
    result.append(binary)
  return result
def binary2string(b):
  result = ""
  for item in b:
    binary1 = item[:8]
    binary2 = item[8:]
    result += chr(int(binary1, 2)) + chr(int(binary2, 2))
  return result
def getIV():
    return '0101'+''.join(random.choice('01') for _ in range(12))
def xor(a,b):
   return ''.join(str((int(x)-48) ^ (int(y)-48)) for x, y in zip(a, b)).zfill(16)
def binary_to_base64(binary):
    return base64.b64encode(binary2string(binary).encode()).decode()
def base64_to_binary(base64_string):
    return string2binary(base64.b64decode(base64_string).decode())
#这些格式转换的函数在exp中可以用，不太建议自己写，可能效果不好
def output_cypher():
    flag = 'here_is_flag_but_I_hide_it_haha~'
    keys ='here_is_key_but_I_cant_give_you~'
    IV = getIV()
    print('initIV:',IV)
    message = string2binary(flag)
    key = string2binary(keys)
    cyphertext=[]
    for i in range(16):
        IV = xor(IV,message[i])
        cyphertext.append(xor(IV,key[i]))
        IV=cyphertext[i]
    print('Cyphertext_Base64:',binary_to_base64(cyphertext))
if __name__=='__main__':
    output_cypher()