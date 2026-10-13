class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        isAllowed = True
        res = 0
        allowed = set(allowed)
        for word in words:
            i = 0

            while i < len(word) and word[i] in allowed:
                i += 1

            if i == len(word):
                res += 1
        
        return res
            
                