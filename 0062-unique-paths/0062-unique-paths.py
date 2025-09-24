class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[n - 1] = 1
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):

                if c + 1 < n:
                    dp[c] += dp[c + 1]

        return dp[0]
                
        