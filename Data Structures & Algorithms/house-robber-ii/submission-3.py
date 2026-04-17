class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    # two options, either rob the first house and not the last
    # or rob the last house and not the first
    # so just call house robber 1 solution on both options and take max
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 
        for n in nums:
            temp = rob2
            rob2 = max(rob1 + n, rob2)
            rob1 = temp
        return rob2
            