class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP Solution: 
        # - start at the end
        # - at each index LIS[i] = max(1, 
        #       if nums[i] < nums[i + k] :
        #           1 + LIS[i + k] for k in range(i + 1, len(nums)))

        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
        