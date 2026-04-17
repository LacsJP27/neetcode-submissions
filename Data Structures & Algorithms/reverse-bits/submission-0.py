class Solution:
    def reverseBits(self, n: int) -> int:
        # i = 0 -> bitlength - 1
        res = 0
        for i in range(32):
            # shift 
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res
        
            