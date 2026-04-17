class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        k = 0
        word_present = False
        visited = {}
        def dfs(i, j, k):
            if k == len(word):
                return True
                
            if (i == ROWS or j == COLS or i < 0 or j < 0 or 
                word[k] != board[i][j] or visited[(i, j)]):
                return False
            
            visited[(i, j)] = True
            k += 1
            res = dfs(i + 1, j, k) or dfs(i -1, j, k) or dfs(i, j - 1, k) or dfs(i, j + 1, k)
            visited[(i,j)] = False
            return res
            
        for i in range(ROWS):
            for j in range(COLS):
                visited[(i, j)] = False
        for i in range(ROWS):
            for j in range(COLS):
                word_present = dfs(i, j, 0)
                if word_present:
                    return True
        return False
        

        

