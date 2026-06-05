class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedu solution
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            # shifting the goal post
            if i + nums[i] >= goal:
                goal = i
        
        # Goal will 0 iff the first index is able to reach the goal
        return True if goal == 0 else False
