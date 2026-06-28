class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        input: int
        output: first int rows of pascal

        edge: input is 1 

        plan:
        have an initial 2 rows in output
        generate other rows by looping through prev row and adding adj numbers, add 1s at start and end
        '''

        if numRows == 1:
            return [[1]]
        
        otp = [[1]]

        for row in range(2, numRows + 1):
            res = []
            prev = otp[-1]

            for j in range(row):
                if j == 0 or j == row - 1:
                    res.append(1)
                else:
                    res.append(prev[j] + prev[j - 1])

            otp.append(res)

        return otp


        '''
        runtime: O(n^2)
        additional space: O(n)
        '''
        