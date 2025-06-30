# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
# 给定两个整数数组gas和cost，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则保证它是唯一的。
# 示例 1:
# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
class GasStation(object):
    def canCompleteCircuit1(self, gas, cost):
        # 95 ms, 14.84 mb
        # 原理：如果i起点，可以到j但是不能到j+1，那么从i+1到j任意一个地方为起点，都不能到j+1
        # 从0开始，如果能到j不能到j+1，则记下差的油toHere，再以j+1为起点，最远到k+1，toHere加上j+1到k+1差的油，直到能到n-1
        # 将到n-1的存油与toHere比较
        n = len(gas)
        i = 0
        toHere = 0
        while(i < n):
            sumGas = 0
            sumCost = 0
            j = i
            while(j < n):
                sumGas += gas[j]
                sumCost += cost[j]
                if sumGas < sumCost:
                    toHere = toHere + sumCost - sumGas
                    break
                j += 1
            if sumGas >= sumCost + toHere:
                return i
            i = j+1
        return -1
    
    def canCompleteCircuit2(self, gas, cost):
        # 85 ms, 17.50 mb
        # 通过画折线图，只有在最低点对应的x为起点才可能成功，同时sumGas>=sumCost
        n = len(gas)
        min = 0
        indexOfMin = 0
        spare = 0
        for i in range(n):
            spare += gas[i] - cost[i]
            if(spare < min):
                min = spare
                indexOfMin = i
        if spare < 0:
            return -1
        if min >= 0:
            return 0
        return (indexOfMin+1)%n



test = GasStation()
# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
gas = [2,3,4]
cost = [3,4,3]
print(test.canCompleteCircuit2(gas, cost))
