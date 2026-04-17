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
            res = max(res, r - l)
            while l < r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1

        return max(res, r - l)
            
