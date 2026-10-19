class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }

        # building the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''

            for j in range(minLen):
            # first differing character
                if w1[j] != w2[j]:
                    # the character at word1 comes before w2
                    adj[w1[j]].add(w2[j])
                    break
        visit = {} # False=visited, True=visited & current path, not in dict means not visited

        res = []

        def dfs(c):
            if c in visit:
                return visit[c] # if true then loop

            visit[c] = True # visited and current path
            
            for nei in adj[c]:
                if dfs(nei):
                    return True

            # new path
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return "" # detected loop


        res.reverse()
        return ''.join(res)




        