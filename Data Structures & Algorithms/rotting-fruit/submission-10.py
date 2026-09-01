class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1. find all the rotten fruit and store in a list, else return -1
        #   list of indices
        # 2. for each rotten fruit in list turn adj fresh fruit rotten 
            # and mark old rotten fruits as visited one level at a time
            # use temp list and once temp empty that's one level
            # make a new list
        # 3. Add 1 to minute count
        # 4. Repeat step 2 until all possible squares visited (rotten)
            # if after an iteration of step 2, new list empty then exit
        # 5. Check if a fresh fruit (1) remains, return -1 else return
            # minute count
            # loop through grid check for a 1
        res = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in        
            range(len(grid))]
        
        rotten = self.findRotten(grid, visited)

            # one level
        while len(rotten) != 0:
            newRotten = []
            for fruit in rotten:
                y = fruit[0]
                x = fruit[1]
                visited[y][x] = True

                if self.isFresh([y + 1, x], grid, visited):
                    grid[y + 1][x] = 2
                    newRotten.append([y + 1, x])

                if self.isFresh([y - 1, x], grid, visited):
                    grid[y - 1][x] = 2
                    newRotten.append([y - 1, x])

                if self.isFresh([y, x + 1], grid, visited):
                    grid[y][x + 1] = 2
                    newRotten.append([y, x + 1])
                    
                if self.isFresh([y, x - 1], grid, visited):
                    grid[y][x - 1] = 2
                    newRotten.append([y, x - 1])

            res += 1
            rotten = newRotten

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    print("IMPOSSIBLE")
                    return -1
        
        print("TEST")
        if not res:
            return 0

        return res - 1


    def findRotten(self, grid, visited):
    
        rotten = []
            
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2 and not visited[y][x]:
                    rotten.append([y, x])
    
        return rotten

    def isFresh(self, index, grid, visited):
        y = index[0]
        x = index[1]

        if (y < 0 or 
            y >= len(grid) or 
            x < 0 or 
            x >= len(grid[0])):

            return False


        if(visited[y][x] or grid[y][x] != 1):
            return False

        return True


            




        