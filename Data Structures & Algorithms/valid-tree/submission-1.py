

class Solution:
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        # adjancency list
        adj = { i:[] for i in range(n)}

        # build adjancency list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        # define the dfs alg
        def dfs(i, prev):
            # check if i in visit
            if i in visit:
                return False
            # dfs the adjancent nodes
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
