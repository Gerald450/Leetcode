class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        input: grid
        output: area of largest 1s square

        edge: no 1s square, no 1s, empty grid

        plan:
        use top bottom dp
        build a square ending at (i, j)
        compare to left and diagonal  and get minimum if they diferent, if all same add one
        if  value is zero set it to infinity
        keep track of the maxLength

        '''

        rows, cols = len(matrix), len(matrix[0])
        dp = [[1 for _ in range(cols)] for _ in range(rows)]

        



        maxLength = 0
        for row in range(rows):
            for col in range(cols):
                checkInf = set([dp[row-1][col], dp[row - 1][col - 1], dp[row][col -1]])

                if matrix[row][col] == "1":
                    maxLength = max(maxLength, 1)
                        
                if matrix[row][col] == "1" and (row != 0 and col != 0) and inf not in checkInf:
                    if dp[row - 1][col] == dp[row][col - 1] == dp[row - 1][col - 1]:
                        dp[row][col] = int(dp[row - 1][col]) + 1


                    else:

                        if col-1 == 0 or row - 1 == 0:
                            dp[row][col] = 2


                        else:
                           
                            minNum = int(min(dp[row - 1][col], dp[row][col - 1],dp[row - 1][col - 1]))
                            maxNum = int(max(dp[row - 1][col], dp[row][col - 1],dp[row - 1][col - 1]))

                            if maxNum - minNum == 1:
                                dp[row][col] = maxNum
                            else:
                                dp[row][col] = minNum + 1
                        

                    maxLength = max(maxLength, dp[row][col])

                elif matrix[row][col] == "0":
                    dp[row][col] = float('inf')


        print(dp)

                


        return maxLength * maxLength


                    

'''
[["1","1","1","0","0"],
 ["1","1","1","0","0"],
 ["1","1","1","1","1"],
 ["0","1","1","1","1"],
 ["0","1","1","1","1"],
 ["0","1","1","1","1"]]


 [[1, 1, 1, inf, inf], 
  [1, 2, 2, inf, inf], 
  [1,   2, 3, 1, 1], 
  [inf, 1, 1, 1, 2], 
  [inf, 1, 2, 2, 2], 
  [inf, 1, 2, 3, 3]]
'''


