class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        isAllowed = True
        res = 0
        for word in words:
            for c in word:
                if c not in allowed:
                    isAllowed = False
            if isAllowed:
                res += 1
            isAllowed = True
        
        return res
            
                