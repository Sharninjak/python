# 20240420-1635
# 给你一个字符串 s ，请你反转字符串中单词的顺序。
# 单词是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的单词分隔开。
# 返回单词顺序颠倒且 单词 之间用单个空格连接的结果字符串。
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

class Solution(object):
    def reverseWords(self, s):
        # 16 ms, 11.79 mb
        """
        :type s: str
        :rtype: str
        """
        s = list(filter(None, s.split(" ")))
        # <==>
        # s = s.split()
        print(s)
        rvs = s[-1]
        num = len(s)
        for i in range(num-2, -1, -1):
            rvs += " " + s[i]
        return rvs

    def reverseWords2(self, s):
        # 10 ms, 11.82 mb
        # 删除前后空白
        s = s.strip()
        # print(s)
        # 反转整个字符串
        s = s[::-1]
        # 将字符串拆分为单词，并反转每个单词
        # print(s)
        # print(s.split())
        # for word in s.split():
        # print(word[::-1])
        s = ' '.join(word[::-1] for word in s.split())
        return s


if __name__=="__main__":
    test = Solution()
    s = "   the    sky is blue   "

    print(test.reverseWords(s=s))
    print(test.reverseWords2(s=s))
    m = "1234"
    n = "asdf".join(m)
    print(n)



