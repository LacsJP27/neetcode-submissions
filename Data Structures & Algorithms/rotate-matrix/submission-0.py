class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # when you rotate the matrix by 90
        # an elements index changes by 2
        # time: O(n^2)
        # memory: O(1) (inplace)
        # set boundaries (l, r, top, bottom)
        # r is the number of columns - 1
        l, r, = 0, len(matrix[0]) - 1
        # we move left and right to adjust for inner matrices
        # that's why this condition works
        while l < r:
            # iterate through the entire row
            for i in range(r - l):
                # because its a square matrix
                top, bottom = l, r
                # save the top left value
                # rotate in reverse (counter-clockwise) -> makes coding easier
                # so rotating counter-clockwise

                # use i to shift for each element
                # draw a picture for visualization of how i is used
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move botom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right:
                matrix[top + i][r] = topLeft
            # shift one layer
            # also shifts top and bottom
            l += 1
            r -=1
