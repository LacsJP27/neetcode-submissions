class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)
        for s in strs:
            strMap[''.join(sorted(s))].append(s)
        return list(strMap.values())



