class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[[str]]:
        # have some map of sorted strings as the keys and the words that go there as the values
        # just iterate through all the values in the map and group by keys
        
        # map should have strings as keys and a list as values
        sameChars = defaultdict(list)

        for word in strs:
            sameChars["".join(sorted(word))].append(word)
        
        res = []
        for groups in sameChars.values():
            res.append(groups)
        return res
        

