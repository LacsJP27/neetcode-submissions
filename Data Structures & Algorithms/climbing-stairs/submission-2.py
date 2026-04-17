class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        res = 1

        for i in range(n - 2, -1, -1):
            res = one + two
            one = two
            two = res
        return res