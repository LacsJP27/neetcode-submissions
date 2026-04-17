class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for num in nums:
            res.add(num)
        return len(res) != len(nums)