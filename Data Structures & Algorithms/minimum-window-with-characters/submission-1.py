class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        # compare the counts of chars in t with counts of chars in window
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        # len(countT) gives the UNIQUE characters in t
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            # does this satisfy the counts of the char in t
            if c in countT and countT[c] == window[c]:
                # one t character's counts all present in window
                have += 1
            while have == need:
                # current length of string window < resLen
                if (r - l + 1) < resLen:
                    # then we found a smaller valid window result
                    res = [l, r]
                    resLen = (r - l + 1)
                    # pop left from the left of our window until 
                    # window invalid (have != need)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -= 1
                # poping left
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
                    
