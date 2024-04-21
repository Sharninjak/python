# https://leetcode.cn/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150
# 135. 分发糖果
# 困难
# 相关标签
# 相关企业
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
# 你需要按照以下要求，给这些孩子分发糖果：
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。


class AllocateCandy(object):
    def candy1(self, ratings):
        # 32 ms, 13.86mb; O(n), O(n)
        arrlen = len(ratings)
        candy = []
        candy.append(1)
        # 满足:分左<右时，糖左<右
        for i in range(arrlen-1):
            if ratings[i] < ratings[i+1]:
                candy.append(candy[i]+1)
            else:
                candy.append(1)
        # print(candy)
        # 在上面的基础上，调整使满足分左>右时，糖左>右
        for i in range(arrlen-1, 0, -1):
        # for i in reversed(range(arrlen)):
            if ratings[i] < ratings[i-1]:
                candy[i-1] = max(candy[i]+1, candy[i-1])
        # print(candy)
        return sum(candy) # 速度快，内存大
        # num = 0
        # for i in range(arrlen):
        #     num += candy[i]
        # return num   # 速度慢，内存小

    def candy2(self, ratings)->int:
        # 我们从左到右枚举每一个同学，记前一个同学分得的糖果数量为 pre
        # 如果当前同学比上一个同学评分高，说明我们就在最近的递增序列中，直接分配给该同学 pre+1
        # 否则我们就在一个递减序列中，我们直接分配给当前同学一个糖果，并把该同学所在的递减序列中所有的同学都再多分配一个糖果，以保证糖果数量还是满足条件。
        # 我们无需显式地额外分配糖果，只需要记录当前的递减序列长度，即可知道需要额外分配的糖果数量。
        # 同时注意当当前的递减序列长度和上一个递增序列等长时，需要把最近的递增序列的最后一个同学也并进递减序列中。
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1
        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1
        return ret



if __name__=="__main__":
    test = AllocateCandy()
    rate = [1,0,2]
    rate = [1,2,2]
    rate = [0,1,2,5,3,2,7]
    rate = [1,2,3,5,4,3,2,1,4,3,2,1]
    # rate = [58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89]
    print(test.candy1(rate))
    print(test.candy2(rate))

