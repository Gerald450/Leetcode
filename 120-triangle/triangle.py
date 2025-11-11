class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        input: that
        output: int

        edge cases: empty, one

        plan:
        start from the bottom, getting the minimum at each index
        start at -2
        return arr[0]

        '''

        dp = triangle[-1]

        for i in range(len(triangle) - 2, -1, -1):

            for j in range(len(triangle[i])):
                dp[j] = min(dp[j] + triangle[i][j], dp[j + 1] + triangle[i][j])

        return dp[0]


        '''
        [[2],[3,4],[6,5,7],[4,1,8,3]]


        [[-10]]
        i = 0
        j = 0

        triangle[0] = [-10]

        dp = [-10]
        





        '''




        