class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l to r already sorted
            # target == mid? then return mid
            # target < mid? then search l to mid - 1
            # else search mid + t to r
        # r is less than l
            # if mid == target return mid
            # if mid < l and target < mid
                # r = mid - 1
                # try l to r again
                # if target > mid and target != l:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # the left is sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid -1
            # the right sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

            

                    
