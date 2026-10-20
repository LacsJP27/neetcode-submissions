class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # O(1)
        h, w = abs(row1 - row2), abs(col1 - col2)
        res = 0

        for row in range(row1, row1 + h + 1, 1):
            res += sum(self.matrix[row][col1:col1 + w + 1])
        
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)