class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)
        res = []

        for s in strs:
            strMap[''.join(sorted(s))].append(s)
        
        for k in strMap:
            res.append(strMap[k])
        return res



