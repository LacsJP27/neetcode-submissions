class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return

        res = [0] * (len(digits) + 1)

        for i in range(len(digits)):
            res[i + 1] = digits[i]

        i = len(digits)
        res[i] += 1

        while res[i] == 10:
            res[i] = 0
            i -= 1
            res[i] += 1

        if res[0] == 1:
            return res
        else:
            return res[1:]