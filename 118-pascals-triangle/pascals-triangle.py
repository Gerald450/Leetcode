class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        input: int
        output: first int rows of pascal

        edge: input is 1 or 2

        plan:
        have an initial 2 rows in output
        generate other rows by looping through prev row and adding adj numbers, add 1s at start and end
        '''

        if numRows == 1:
            return [[1]]
        
        otp = [[1]]

        for i in range(2, numRows + 1):
            res = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    res.append(1)
                else:
                    prev = otp[-1]
                    res.append(prev[j] + prev[j - 1])

            otp.append(res)

        return otp
        