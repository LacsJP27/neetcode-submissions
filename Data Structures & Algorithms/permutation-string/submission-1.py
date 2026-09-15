class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1)
        target = {}
        for c in s1:
            target[c] = target.get(c, 0) + 1

        while j <= len(s2):
            submap = {}
            for c in s2[i:j]:
                submap[c] = submap.get(c, 0) + 1
            if submap == target:
                return True
            j += 1
            i += 1
        
        return False
