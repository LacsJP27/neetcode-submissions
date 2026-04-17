class Solution:
    def hammingWeightWrong(self, n: int) -> int:
        # 13 / 2  = 6 R 1
        # 6/ 2 = 3 R 0
        # 3 / 2 = 1 R 1
        # 1 / 2 = 0 R 1
        # 1101
        remainder = [n % 2]
        quotient = n // 2

        while quotient != 0:
            remainder.append(quotient % 2)
            quotient = quotient // 2
        res = 0
        for num in remainder:
            if num == 1:
                res += 1
        return res
    def hammingWeight(self, n: int) -> int:
    
        res = 0
        while n: # 101
            res += n & 1
            n >>= 1
        return res


            