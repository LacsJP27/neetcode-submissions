class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # iterate backwards here
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                # once a word is found that matches part of string
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # first match only true if it reaches len(s)
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
                
