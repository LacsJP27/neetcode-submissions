class Solution:

    def encode(self, strs: List[str]) -> str:
        # put length and hastag after to read length of string
        res = ""
        for item in strs:
            res += str(len(item)) + "#" + item
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        # look for length
        # read up to length
        # add to result list
        i = 0
        j = 0
        res = []
        while i < len(s):
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            j = i + 1
            i = j + length
            res.append(s[j:i])
            j = i
        
        return res

            
