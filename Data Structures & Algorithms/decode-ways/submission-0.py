class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = dp[i + 1] + dp[i + 2]
        dp = { len(s) : 1 }
        def dfs(i):
            # already cached
            # or i is the last position in the string
            if i in dp:
                return dp[i]
            # if not end of string
            # if starts with 0 then it's invalid
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            
            # there are some cases with i + 2 valid
            # any two digit number valid starting with 1
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)

