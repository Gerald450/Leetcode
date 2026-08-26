class Solution:
    def numSquares(self, n: int) -> int:
        '''
        input: int
        output: int

        edge: <= 0

        plan:
        
        '''

        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                square = j * j
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]
        