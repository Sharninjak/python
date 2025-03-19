# https://leetcode.cn/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
import string


class Solution:
    def isPalindrome(self, s) -> bool:
        # leetcode不能用import
        s = s.lower()
        # print(s)
        translator = s.maketrans('', '', string.punctuation)
        no_punct = s.translate(translator)
        # print(no_punct)
        no_space = no_punct.replace(' ', '')
        # print(no_space)
        i = 0
        j = len(no_space)-1
        # 双指针判断
        while i < j:
            if no_space[i] != no_space[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    
    def isPalindrome2(self, s) -> bool:
        # 35 ms, 13.71 mb
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        # 翻转判断
        return sgood == sgood[::-1]

    def isPalindrome3(self, s) -> bool:
        # 41 ms, 11.78 mb
        # 相较于2，空间为O(1)，没有新创一个字符串
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True


if __name__=="__main__":
    test = Solution()
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    s = " "
    print(test.isPalindrome(s=s))
    print(test.isPalindrome2(s=s))
    print(test.isPalindrome3(s=s))
