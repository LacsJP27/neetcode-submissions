class Solution:
    #given two string s and t
    # return true if strings are anagrams
    # otherwise return false
    # anagram is as string that contains the exact same characters as another string and 
    # order can be different
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        return sortedS == sortedT
