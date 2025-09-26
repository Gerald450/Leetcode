class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1) + 1
        cols = len(word2) + 1
        dp = [[float('inf')] * cols for i in range(rows)]
        

        for i in range(len(word2) + 1):
            dp[-1][i] = len(word2) - i
        for j in range(len(word1) + 1):
            dp[j][-1] = len(word1) - j


        for r in range(len(word1) - 1, -1, -1):
            for c in range(len(word2) - 1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    #min of all 3 operations
                    dp[r][c] = 1 + min(dp[r+1][c], dp[r][c + 1], dp[r + 1][c + 1])

        return dp[0][0]


        

        