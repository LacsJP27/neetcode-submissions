class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using set length
        # return len(set(nums)) != len(nums)

        # python uses powersort
        # sorting here is O(nlogn) worst case
        # space complexity is O(n) worst case and O(1) if array nearly sorted
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
