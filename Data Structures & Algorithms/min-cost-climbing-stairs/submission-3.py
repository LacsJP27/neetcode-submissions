class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # start at i = 0:
        # if 
        # cost(i = 0): 1 + min(cost(i = 1) + cost(i = 2))
        dp = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if dp[i] != -1 :
                return dp[i]

            dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return dp[i]

        dfs(0)
        return min(dp[0], dp[1])

        