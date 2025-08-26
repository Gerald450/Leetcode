class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        res = [float('inf')] * (cols)
        res[cols-1] = 0

        for r in range(rows -1, -1, -1):
            valR = float('inf')
            for c in range(cols - 1, -1, -1):
                res[c] = grid[r][c] + min(valR, res[c])
                valR = res[c]
            

        return res[0]
        