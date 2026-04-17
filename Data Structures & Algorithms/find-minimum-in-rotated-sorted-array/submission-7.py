class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (r + l) // 2
            # think about this array [4, 5, 1, 2, 3]
            # right and left will both go to 5 and break
            # 1 will never be stored as min without the line below
            res = min(res, nums[mid])
            # nums[l] > nums[r]
            if nums[l] <= nums[mid]:
                # from l to mid the values are greater than num[r]
                # move past this point
                l = mid + 1
            else:
                # the minimum may be at mid or before
                # so move r 
                # can do this since checking if the mid is the min before
                r = mid - 1
        return res

