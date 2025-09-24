class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * col
        dp[col - 1] = 1

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < col:
                    dp[c] += dp[c + 1]
        
        return dp[0]
        