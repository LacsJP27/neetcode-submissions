class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        # windlength - count[max] is the number of replacements to get same substring
        # check number of replacements <= k this is the condition we need to check
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            # how to get max value in a hashmap (the most common character)
            # window length - most frequent character
            if (r - l + 1) - max(freq.values()) > k:
                # decrement the count for the character at the old left position (not in window)
                freq[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res


