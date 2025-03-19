# 整数转罗马数字
# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
# 数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，
# 数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给你一个整数，将其转为罗马数字。
class IntToRoman(object):
    def intToRoman1(self, num):
        # leecode 的list顺序是反过来的，且不能用reversed: TypeError: argument to reversed() must be a sequence
        VALUE_SYMBOLS={
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        string = ""
        for i in VALUE_SYMBOLS:
            # print(i,VALUE_SYMBOLS[i])
            while num >= i:
                num -= i
                string += VALUE_SYMBOLS[i]
            if num == 0:
                break
        return string
    
    def intToRoman2(self, num):
        # 45 ms, 11.44 mb
        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        ans = ""
        for value, symbol in VALUE_SYMBOLS:
            while num >= value:
                num -= value
                ans += symbol
            if num == 0:
                break
        return ans
    
    def intToRoman3(self, num):
        # 39 ms, 11.50 mb
        # I:1， V:5， X:10， L:50， C:100，D:500, M:1000
        ans = ""
        n1 = num // 1000
        ans += "M"*n1

        num -= 1000*n1
        n2 = num // 100
        if n2 == 9:
            ans += "CM"
        elif n2 == 4:
            ans += "CD"
        else:
            ans += "D"*(n2//5)+"C"*(n2%5)
        

        num -= 100*n2
        n3 = num // 10
        if n3 == 9:
            ans += "XC"
        elif n3 == 4:
            ans += "XL"
        else:
            ans += "L"*(n3//5)+"X"*(n3%5)

        num -= 10*n3
        n4 = num
        if n4 == 9:
            ans += "IX"
        elif n4 == 4:
            ans += "IV"
        else:
            ans += "V"*(n4//5)+"I"*(n4%5)
        return ans


if __name__=="__main__":
    test= IntToRoman()
    num = 1994
    num = 58
    print(test.intToRoman1(num))
    print(test.intToRoman2(num))
    print(test.intToRoman3(num))