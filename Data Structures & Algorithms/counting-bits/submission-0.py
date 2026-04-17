class Solution:
    def countBits(self, n: int) -> List[int]:
        # 3
        # i: 0, 1, 10, 11
        # res: [0, 1, 1, 2]
        res = []
        for i in range(n + 1):
            binaryNum = bin(i)
            ones = 0
            while i:
                ones += i & 1
                i >>= 1
            res.append(ones)
        return res