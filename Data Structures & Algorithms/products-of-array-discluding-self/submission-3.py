class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 3 4
        # 24 12 8 6
        # O(n^2) solution would be nested loop and just continue if i = j
        prepend = 1
        i = 0
        res = [1] * len(nums)
        while i in range(len(nums)):
            if i > 0:
                prepend *= nums[i - 1]
            res[i] = prepend
            i += 1
        i = len(nums) - 1
        append = 1
        while i >= 0:
            if i < len(nums) - 1:
                append *= nums[i + 1]
            res[i] *= append
            i -= 1
        return res

        
