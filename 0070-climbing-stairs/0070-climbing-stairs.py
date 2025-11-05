class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = 5
        dp[5] = 1
        dp[4] = 1
        dp[3] = 2
        dp[2] = 3
        dp[1] = 5
        dp[0] = 8

        '''
        first, second = 1, 1

        for i in range(n - 1):
            temp = first + second
            first = second
            second = temp

        return second



        