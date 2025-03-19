# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度
# 单词是指仅由字母组成、不包含任何空格字符的最大子字符串

class Solution(object):
    def lengthOfLastWord1(self, s):
        # 8 ms, 11.55 mb
        n = len(s)-1
        while s[n] == " " and n >= 0:
            n -= 1
        length = 0
        while s[n] != " " and n >= 0:
            n -= 1
            length += 1
        return length

    def lengthOfLastWord2(self, s):
        # 12 ms, 11.48 mb
        s = list(filter(None, s.split(" ")))
        # print(s)
        return len(s[-1])

def is_moon(s):
    return s != "moon"

def is_odd(n):
    return n % 2 == 1



if __name__=="__main__":
    test = Solution()
    s = "Hello World"
    s = "   fly me   to   the moon  "
    print(test.lengthOfLastWord1(s))
    print(test.lengthOfLastWord2(s))
    # newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # print(newlist)
