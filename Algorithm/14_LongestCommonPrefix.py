# 20240420
# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
class Solution(object):
    def longestCommonPrefix(self, strs):
        # 15 ms, 11.59 mb
        """
        :type strs: List[str]
        :rtype: str
        """
        num = len(strs)
        if num == 1:
            return strs[0]
        n = len(strs[0])
        # for i in range(num):
        #     if len(strs[i]) < n:
        #         n = len(strs[i])
        # <==>
        n = len(min(strs, key=len))
        if n == 0:
            return ""
        count = ""
        for i in range(n):
            x = strs[0][i]
            for j in range(1, num):
                if strs[j][i] != x:
                    return count
                if j == num - 1:
                    count += x
        return count
    
        


if __name__=="__main__":
    test = Solution()
    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    # strs = ["a"]
    strs = ["","b"]
    print(test.longestCommonPrefix(strs=strs))

