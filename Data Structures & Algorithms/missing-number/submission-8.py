class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        #[0, 1, 3]
        # n = 3
        # [0, 1, 2, 3]
        for i in range(n):
            if nums[i] != i:
                return i
        return n
