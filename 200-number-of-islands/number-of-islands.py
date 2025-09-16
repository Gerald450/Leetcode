class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        seen = set()


        def dfs(r,c):
            if grid[r][c] == '0' or (r,c) in seen:
                return

            seen.add((r,c))

            directions = [[1,0], [0,1], [-1,0], [0,-1]]

            for direction in directions:
                dr, dc = direction
                row, col = r + dr, c + dc
                
                if ((row, col) not in seen and
                    row in range(0, rows) and
                    col in range(0, cols) and
                    grid[row][col] == '1'):

                    dfs(row, col)
                    seen.add((row, col))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    islands += 1
                    dfs(r, c)

        return islands