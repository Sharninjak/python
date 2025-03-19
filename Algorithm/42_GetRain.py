# https://leetcode.cn/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

class GetRain(object):
    def trap1(self, height):
        # 动态规划
        # 107 ms, 12.8 mb
        n = len(height)
        if n == 0:
            return 0
        # 右边的水不会到左边
        left = [height[0]]
        for i in range(1, n):
            left.append(max(left[i-1], height[i]))
        # print(left)
        # 左边的水不会到右边
        right = [0]*(n-1) + [height[n-1]]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        # print(right)
        ans = sum(min(left[i], right[i]) - height[i] for i in range(n))
        return ans
    
    def trap2(self, height):
        # 单调栈？？？？
        # 23 ms, 12.56 mb
        left,right =0, len(height)-1
        left_max,right_max = height[0],height[-1]
        water_sum = 0
        while left<=right:
            if left_max<right_max:
                if height[left] < left_max:
                    water_sum+=(left_max-height[left])
                    left+=1
                else:
                    left_max = height[left]
                    left+=1
            else:
                if height[right] < right_max:
                    water_sum+=(right_max-height[right])
                    right-=1
                else:
                    right_max = height[right]
                    right-=1
        return water_sum


if __name__=="__main__":
    test = GetRain()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    print(test.trap1(height))
    print(test.trap2(height))