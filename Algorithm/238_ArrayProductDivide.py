# https://leetcode.cn/problems/product-of-array-except-self/submissions/522297702/?envType=study-plan-v2&envId=top-interview-150
class ArrayProductDivide(object):
    def productExceptSelf1(self, nums):
        answer = []
        numsLen = len(nums)
        for i in range(numsLen):
            temp = 1
            for j in range(numsLen):
                if j!=i:
                    temp *= nums[j]
            answer.append(temp)
        return answer
    
    def productExceptSelf2(self, nums):
        # 使用了除法
        answer = []
        numsLen = len(nums)
        before = 1
        for i in range(1, numsLen):
            before *= nums[i]
        answer.append(before)
        for i in range(1, numsLen):
            before = before / nums[i] * nums[i-1]
            answer.append(before)
        return answer
    
    def productExceptSelf3(self, nums):
        # 74 ms, 21.26 MB
        numsLen = len(nums)
        answer = []
        left = [1]*numsLen
        right = [1]*numsLen
        # print(left)
        for i in range(1, numsLen):
            left[i] = left[i-1]*nums[i-1]
        for i in range(numsLen-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        for i in range(numsLen):
            answer.append(left[i]*right[i])
        return answer
    
    def productExceptSelf4(self, nums):
        # 60 ms, 20.63 MB; O(N),O(N)
        numsLen = len(nums)
        answer = []
        # left = [1]*numsLen
        right = [1]*numsLen
        # print(left)
        # for i in range(1, numsLen):
        #     left[i] = left[i-1]*nums[i-1]
        for i in range(numsLen-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        answer.append(right[0])
        left = 1
        for i in range(1, numsLen):
            left *= nums[i-1]
            answer.append(left*right[i])
        return answer
    
    def productExceptSelf5(self, nums):
        # 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）
        # 58 ms, 19.26 MB; O(N),O(1)
        numsLen = len(nums)
        answer = [1]*numsLen
        for i in range(numsLen-2, -1, -1):
            answer[i] = answer[i+1]*nums[i+1]
        left = 1
        for i in range(1, numsLen):
            left *= nums[i-1]
            answer[i] = left*answer[i]
        return answer


    
if __name__=="__main__":
    test = ArrayProductDivide()
    # nums = [-1,1,0,-3,3]
    nums = [1,2,3,4]
    print(test.productExceptSelf5(nums))
    # length = len(nums)
    # print(length)
    # for i in range(length):
    #     print(nums[i])
