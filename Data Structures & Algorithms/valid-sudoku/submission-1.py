class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows:
                    return False
                rows.add(board[r][c])
            rows.clear()
        for c in range(9):
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in cols:
                    return False
                cols.add(board[r][c])
            cols.clear()

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                i, j = r, c
                while i < r + 3:
                    j = c
                    while j < c + 3:
                        if board[i][j] in boxes:
                            return False
                        if board[i][j] != '.':
                            boxes.add(board[i][j])
                        j += 1
                    i += 1
                boxes.clear()
        
        return True
            
                