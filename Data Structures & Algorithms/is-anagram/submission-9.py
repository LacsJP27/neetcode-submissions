class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        tChars = {}

        for c in s:
            sChars[c] = sChars.get(c, 0) + 1
        for c in t:
            tChars[c] = tChars.get(c, 0) + 1
        
        return sChars == tChars


