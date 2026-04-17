class Solution:
    def maxSubArrayBruteForce(self, nums: List[int]) -> int:
        maxSum = -float("inf")
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                maxSum = max(maxSum, sum(nums[i:j+1]))
        return maxSum
    
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float("inf")
    # # [2,-3,4,-2,2,1,-1,4]
    #     i   j      k    l
    #     maxSum = 2, 2, 4, 5, 8 
    #     currSum = 2, -1, 4, 2
    #    2 -3, 4
        currSum = 0
        maxSub = nums[0]

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub

