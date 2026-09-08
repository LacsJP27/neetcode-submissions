class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        # [1, 2, 3, 4], target = 5
        def dfs(i, curr, total):
            #i: 0, 1, 
            #curr: [], [1] [], [1, 2] [1] [2] []
            #total: 0, 1 0, 3 1 2 0
            if total == target:
                res.append(curr.copy())
                return

            if total > target:
                return

            if i >= len(candidates):
                return



            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        

        return res
             