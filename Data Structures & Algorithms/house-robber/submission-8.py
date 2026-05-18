class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        # top-down
        def dfs(k):
            if k >= len(nums):
                return 0

            if dp[k] != -1:
                return dp[k]

            dp[k] = max(nums[k] + dfs(k +2 ), dfs(k + 1))
            return dp[k]

        return dfs(0)