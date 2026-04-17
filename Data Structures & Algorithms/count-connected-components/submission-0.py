class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        # adjancency list
        adj = {i:[] for i in range(n)}

        # visited set
        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(i):
            for j in adj[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)
            
        res = 0
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res+=1

        return res
            
