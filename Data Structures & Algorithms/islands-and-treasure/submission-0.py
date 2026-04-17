class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addLayer(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visit:

                return
            q.append([r,c])
            visit.add((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # initialize queue with gates
                    q.append([r, c])
                    # update the visit set
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                # modify the pos with the distance away from gate
                grid[r][c] = dist

                #increment layer by one
                addLayer(r + 1, c)
                addLayer(r - 1, c)
                addLayer(r, c + 1)
                addLayer(r, c - 1)
            # increment distance by one after each layer
            dist += 1


