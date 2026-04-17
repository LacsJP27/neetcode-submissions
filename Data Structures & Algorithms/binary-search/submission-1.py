
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(l, r, key):
            if l > r:
                return -1
            mid = l + (r - l) // 2
            if nums[mid] == key:
                return mid
            elif key > nums[mid]:
                return binarySearch(mid + 1, r, key)
            else:
                return binarySearch(l, mid - 1, key)
        
        return binarySearch(0, len(nums) - 1, target)

        
