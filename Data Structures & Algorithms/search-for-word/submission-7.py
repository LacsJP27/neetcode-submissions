class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r >= ROWS or r < 0) or (c >= COLS or c < 0) or visited[r][c]:
                return False

            visited[r][c] = True
            res = False
            if board[r][c] == word[i]:
                i += 1
                res = dfs(r + 1, c, i) or dfs(r - 1, c, i) or dfs(r, c + 1, i) or dfs(r, c - 1, i)

            visited[r][c] = False

            return res

        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r, c, 0)
                if res == True:
                    return True

        return False