class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsToIdx = {}
        for i in range(len(nums)):
            numsToIdx[nums[i]] = i
        for i in range(len(nums)):
            num = target - nums[i]
            if num in numsToIdx.keys() and i != numsToIdx[num]:
                return [i, numsToIdx[num]]