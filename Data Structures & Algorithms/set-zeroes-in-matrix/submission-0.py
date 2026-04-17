class Solution:
    # time: O(m*n) space: O(m + n)
    def setZeroesArrays(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(ROWS):
            for c in range(COLS):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        # need this so rows and cols don't overlap inplace
        rowZero = False

        # determine which rows and cols need zeroes
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # keep track of which cols need zeroes using top row
                    matrix[0][c] = 0
                    # to make sure the row and cols markers don't overlap
                    if r > 0:
                        # set the first column to keep track of zero rows
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        # zeroing the matrix out
        # skip the first row and column (where they intersect so we don't overried the mark)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                # zero out first column
                matrix[r][0] = 0
        if rowZero:
            # zero out the row
            # now notice why you need this extra var
            for c in range(COLS):
                matrix[0][c] = 0
    