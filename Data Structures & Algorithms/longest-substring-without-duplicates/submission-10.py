class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        seen = set()
        l, r = 0, 1
        seen.add(s[l])
        res = 0

        while r < len(s):
            while l < r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res
            
