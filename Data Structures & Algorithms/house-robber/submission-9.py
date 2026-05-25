class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = [0, 0, 14, 6, 0]
        memo = [0 for _ in range(len(nums))]

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i]:
                return memo[i]
            if i == len(nums) - 1:
                memo[i] = nums[i]
                return nums[i]
            # dfs(2): 8 + 6 or 6
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i+1))
            return memo[i]
        
        return dfs(0)