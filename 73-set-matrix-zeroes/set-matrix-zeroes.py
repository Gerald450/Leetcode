class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        rowZero = False
        #determine what needs to be zero
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        #change the r, c to zeros
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        #handle matrix[0][0]
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
        
        if rowZero == True:
            for c in range(col):
                matrix[0][c] = 0

        
        
        