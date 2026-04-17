class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # inputs always satisfy the condition
        # twoSum([3, 4, 5, 6], 7)
        # 7 - 3 = 4 -> if 4 is in the array then return index of 4
        # brute force would be nested loops then just add til reach target and check i and j don't equal
        # better solution -> map value to index, loop through nums and check for difference in map
        # return index or map[value]

        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in indices:
                if i != indices[dif]:
                    return [i, indices[dif]]
            