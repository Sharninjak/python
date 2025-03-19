# 20240420-1704
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);

class Solution(object):
    def convert(self, s, numRows):
        # 超出时间限制
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        # circulation: 2 numRows -2
        circulNum =  2 * numRows - 2 # 一次循环字符个数
        # print("一次循环字符个数",circulNum)
        strLen = len(s) # 原字符串长度
        circul = strLen // circulNum + 1  # 循环次数
        # print("循环次数", circul)
        # arr = [['']*numRows]*(numRows-1)*circul
        arr = [['' for i in range((numRows-1)*circul)] for j in range(numRows)]
        # print(arr)
        index = 0
        for i in range(circul):
            for j in range(numRows-1):
                arr[j][i*(numRows-1)] = s[index]
                index += 1
                if index>=strLen:
                    break
            if index>=strLen:
                    break
            for j in range(numRows-1):
                arr[numRows-1-j][i*(numRows-1)+j] = s[index]
                index += 1
                if index>=strLen:
                    break
            if index>=strLen:
                    break
        # print(arr)
        convert = ''
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                convert += arr[i][j]
        return convert

    def convert2(self, s, numRows):
        # 257 ms, 23.07 mb
        # convert的小优化，逻辑没有区别
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2  # 一次循环字符个数
        c = (n + t - 1) // t * (r - 1)  # 需要多少列
        mat = [[''] * c for _ in range(r)]
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < r - 1:  # 每个循环，前n-1个向下，后n-1个向右上
                x += 1  # 向下移动
            else:
                x -= 1
                y += 1  # 向右上移动
        # print(mat)
        print(list(ch for row in mat for ch in row if ch))
        return ''.join(ch for row in mat for ch in row if ch)
    
    def convert3(self, s, numRows):
        # 47 ms, 16.41 mb
        #用一个列表来回跑代替奉二维列表
        if numRows<2:
            return s 
        res = ["" for _ in range(numRows)]
        print(res)
        i , flag = 0,-1
        for c in s:
            res[i] += c
            print(res)
            if i == 0 or i ==numRows-1:
                flag = -flag
            i+=flag
        return "".join(res)


if __name__=="__main__":
    test = Solution()
    s = "PAYPALISHIRING"
    numRows = 4
    print(test.convert(s=s, numRows=numRows))
    print(test.convert2(s=s, numRows=numRows))
    print(test.convert3(s=s, numRows=numRows))

