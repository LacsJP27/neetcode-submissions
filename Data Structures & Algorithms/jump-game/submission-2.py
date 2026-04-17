class Solution:
    def canJumpRecursion(self, nums: List[int]) -> bool:
        def dfs(i): # 
            if i == len(nums) - 1:
                return True
            reachEnd = False
            jumpLen = nums[i]
            for j in range(1, jumpLen + 1): # m = jumplen O(m), 
                reachEnd = dfs(i + j) #O(n!)
                if reachEnd:
                    return True
            return False
        return dfs(0)
    # time complexity of O(n!)

    def canJump(self, nums: List[int]) -> bool:
        
        # [1,2,0,1,0 |]

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            # can the number before the end reach the goal?
            if i + nums[i] >= goal:
                # if yes then see if you can even reach that number
                goal = i
        # goal will be 0 if from goal you could reach the end
        return goal == 0



