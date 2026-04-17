class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for i in range(len(nums)):
            indices[nums[i]] = i

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in indices:
                if i != indices[dif]:
                    return [i, indices[dif]]
        return []

        
        
            