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
            temp = 0
            if (num - 1) not in numSet:
                temp += 1
                nextNum = num + 1
                while nextNum in numSet:
                    temp += 1
                    nextNum += 1
            res = max(res, temp)
        return res

            
            
            

