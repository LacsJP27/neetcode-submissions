class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSrtd  = sorted(s)
        tSrtd = sorted(t)

        print(sSrtd)
        print(tSrtd)

        for i in range(len(s)):
            if sSrtd[i] != tSrtd[i]:
                return False
        
        return True
