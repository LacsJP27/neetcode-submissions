class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
            seen.clear()
        for c in range(9):
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
            seen.clear()

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                i, j = r, c
                while i < r + 3:
                    j = c
                    while j < c + 3:
                        if board[i][j] in seen:
                            return False
                        if board[i][j] != '.':
                            seen.add(board[i][j])
                        j += 1
                    i += 1
                seen.clear()
        
        return True
            
                