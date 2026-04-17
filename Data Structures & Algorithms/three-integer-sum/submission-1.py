class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # you get can get the two sum by seeing if difference between target and num is in array
        # target here is 0
        # return the values at i, j, k (all distinct)
        # we could have i, j right next to each other then find k where i + j = k
        # you could do this in O(n^3)
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            # if i isn't zero
            if i and nums[i] == nums[i - 1]:
                continue
            # now just two sum
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                # the target exists in the arrary
                if count[target] > 0: 
                    res.append([nums[i], nums[j], target])
            # reset the presence of the numbers since you removed the in loop above each visit
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1 

        return res

    def threeSumPointers(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # three sum not possible
            if a > 0:
                break
            # skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            # when sorting you can increase by moving l if needed and decrease by moving r if needed
            # do this for every a.
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
        
                
