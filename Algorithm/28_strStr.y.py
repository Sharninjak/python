class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 41 ms, 16.30 mb
        len1 = len(needle)
        len2 = len(haystack)
        for i in range(len2 - len1 + 1):
            flag = 0
            for j in range(len1):
                if needle[j] == haystack[i+j]:
                    flag += 1
                if flag == len1:
                    return i
        return -1
    
    def strStr2(self, haystack: str, needle: str) -> int:
        # 36 ms, 16.32 mb
        # 比较串而非一个一个比较字符
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
        return -1
    
    def strStr3(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1
        return haystack.find(needle)
    
if __name__=="__main__":
    test = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    haystack = "leetcode"
    needle = "leeto"
    print(test.strStr(haystack=haystack, needle=needle))
    print(test.strStr2(haystack=haystack, needle=needle))
    print(test.strStr3(haystack=haystack, needle=needle))