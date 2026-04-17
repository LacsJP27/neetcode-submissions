class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # a = current num[i]
            # three sum not possible list is sorted
            if a > 0:
                break

            #skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            # when sorted, increase sum by moving l, decrease by moving r
            # do this for every a

            l, r = i + 1, len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # move on two next combination
                    l += 1
                    r -= 1
                    # skip duplicates again
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
