class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # iterate through all chars in str
        for i in range(len(s)):
            # odd length
            l, r = i, i
            # check if substring palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                # expand right and left
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            # check palindrome
            while l >= 0 and r < len(s) and s[l] and s[l] == s[r]:
                # expand right and left
                res += 1
                l -= 1
                r += 1

        return res
