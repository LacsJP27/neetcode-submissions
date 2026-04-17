
class Solution:
    def binarySearch(self, left, right, nums, key) -> int:
        mid = left + (right - left) // 2

        if left > right:
            return -1
        if nums[mid] == key:
            return mid
        if key < nums[mid]:
            return self.binarySearch(left, mid - 1, nums, key)
        else:
            return self.binarySearch(mid + 1, right, nums, key)

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        return self.binarySearch(left, right, nums, target)

        
