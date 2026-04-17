class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        #[0, 1, 3]
        # n = 3
        # [0, 1, 2, 3]
        i, j = 0,0
        while i < n + 1:
            if j >= len(nums):
                return i
            if i != nums[j]:
                return i
            i += 1
            j += 1
            
        return -1
