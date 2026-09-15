class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dupes = set()

        for num in nums:
            if num in dupes:
                dupes.remove(num)
            else:
                dupes.add(num)
            
        return next(iter(dupes))