class Solution:
    def longestPalindrome(self, s: str) -> str:
        # using a dynamic programming solution
        resIdx, resLen = 0, 0

        # dp table to keep tabulate palindrome indices
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i,len(s)):
                # j - i <= 2 is for when i and j start at same index
                # or are only at most 2 positions away from each other
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
        
        return s[resIdx : resIdx + resLen]


