class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minNum = min(nums[r], nums[l])
        while r >= 0:
            if nums[r] > nums[l] :
                minNum = nums[l]
                break;
            l = r
            r -= 1
        return minNum
            

