class Solution:
    def encode(self, strs: List[str]) -> str:
        # list of strings to single string
        # have a number with length
        # a delimitter to indicate when number ends
        # place at beginning of string
        res = ""
        for s in strs:
            length = len(s)
            delimitter = '#'
            res += str(length) + '#' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        # string to list of string, the original list  
        delimitter = '#'
        res = []
        i, j = 0, 0
        while i in range(len(s)):
            while s[j] != delimitter:
                j += 1
            print(s[i:j])
            length = int(s[i:j])
            i = j + 1
            j = i
            while j < (i + length):
                j += 1
            res.append(s[i: j])
            i = j
        return res


