class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        tChars = {}

        for c in s:
            sChars[c] = 1 + sChars.get(c, 0)
        for c in t:
            tChars[c] = 1 + tChars.get(c, 0)
        
        return sChars == tChars


