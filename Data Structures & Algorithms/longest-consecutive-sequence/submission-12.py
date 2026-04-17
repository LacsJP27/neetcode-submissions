class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a number is consecutive if 
        # we could sort it but that's O(nlogn)
        # [2, 20, 5, 10, 3, 4, 5]
        # res = 1, 2, 3, 4
        # [2, 20, ]
        numSet = set(nums)
        res = 0
        for num in nums:
            length = 0
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
            res = max(res, length)
        return res

            
            
            

