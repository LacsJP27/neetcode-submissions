class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                # left sorted portion if the l value 
                # is < the mid value
                if target > nums[mid] or target < nums[l]:
                    # then search the right
                    # not possible for target to be in left portion
                    l = mid + 1
                else:
                    # means the target < nums[mid] and target > nums[l]
                    # l < target < mid
                    r = mid -1
            # right portion is sorted
            # left > mid
            else:
                if target < nums[mid] or target > nums[r]:
                    # target greater than right most value
                    # target less then the middle
                    # target in l to mid
                    r = mid - 1
                else:
                    # target > mid and less than r
                    # mid < target < r
                    l = mid + 1
        return -1

            

                    
