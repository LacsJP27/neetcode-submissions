class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i == len(nums) - 1:
                return True
            reachEnd = False
            jumpLen = nums[i]
            for j in range(1, jumpLen + 1):
                reachEnd = dfs(i + j)
                if reachEnd:
                    return True
            return False
        return dfs(0)

# 

