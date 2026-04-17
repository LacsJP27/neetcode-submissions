class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float("inf")
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                maxSum = max(maxSum, sum(nums[i:j+1]))
        return maxSum