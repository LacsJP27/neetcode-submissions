class Solution:
    def isHappy(self, n: int) -> bool:
        # is an integer defined by
        # sum of square of its digits
        # repeat until number equals 1
        # if stops at one then happy

        # if the sum of the squares = 1 then return true
        # sum of squares the sum of the squares
        # if we've seen the sum of squares before, then return false


        squaresSum = self.sumOfSquares(n)
        seen = set()
        while squaresSum not in seen:
            seen.add(squaresSum)
            if squaresSum == 1:
                return True
            squaresSum = self.sumOfSquares(squaresSum)
        return False
    
    # square all the digist in n
    # sum all these squars
    def sumOfSquares(self, n):
        digits = [int(digit) for digit in str(n)]
        total = 0
        for digit in digits:
            total += digit**2
        return total



