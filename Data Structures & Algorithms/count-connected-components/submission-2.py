class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS Solution
        # res = 0

        # # adjancency list
        # adj = {i:[] for i in range(n)}

        # # visited set
        # visited = set()

        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)

        # def dfs(i):
        #     for j in adj[i]:
        #         if j not in visited:
        #             visited.add(j)
        #             dfs(j)
            
        # res = 0
        
        # for i in range(n):
        #     if i not in visited:
        #         visited.add(i)
        #         dfs(i)
        #         res+=1

        # return res

        # Disjoint Set Union (Rank | Size)

        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                # before going to parent set our parent to the grandparent
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


