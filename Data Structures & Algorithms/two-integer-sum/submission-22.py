class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}

        for i in range(len(nums)):
            numToIndex[nums[i]] = i
        
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in numToIndex:
                if i != numToIndex[partner]:
                    return [i, numToIndex[partner]]