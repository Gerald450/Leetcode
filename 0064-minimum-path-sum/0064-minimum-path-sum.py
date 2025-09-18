class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        arr = [float('inf')] * len(grid[0])
        arr[-1] = 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if c == cols - 1:
                    arr[c] = grid[r][c] + arr[c]
                else:
                    arr[c] = grid[r][c] + min(arr[c], arr[c + 1])
       

        return arr[0]

        