class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        proper = [0] * (len(nums) + 1)
        nums.sort()
        #[0, 1, 3]
        # n = 3
        # [0, 1, 2, 3]
        for i in range(n + 1):
            proper[i] = i
        i, j = 0,0
        while i < len(proper):
            if j >= len(nums):
                return i
            if proper[i] != nums[j]:
                return i
            i += 1
            j += 1
            
        return -1
