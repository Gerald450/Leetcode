class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False



        rows, cols = len(s1) + 1, len(s2) + 1

        dp = [[False] * cols for r in range(rows)]
        dp[-1][-1] = True


        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if r < len(s1) and s1[r] == s3[r + c] and dp[r + 1][c]:
                    dp[r][c] = True
                if c < len(s2) and s2[c] == s3[r + c] and dp[r][c + 1]:
                    dp[r][c] = True
        
        return dp[0][0]

        