class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
    # [ 1, 3, 5, 7, 9, 11, 13]
    # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    # [rob1, rob2, 1, 1, 3, 3]
    #  1st
        # temp: 1
        # rob1: 0
        # rob2: 1
    # 2nd
        # temp: 1
        # rob1: 1
        # rob2: 1
    #3rd
        # temp: 4
        # ~: 1
        # ~: 4
    #4th
        # ~: 4
        # ~: 4
        # ~: 4
    # return rob2 -> 4