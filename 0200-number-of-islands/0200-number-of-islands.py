class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        input: grid matrix
        output: int num of islands

        edge: 

        plan:
        traverse all connected 1's, add to island, put in hashset to avoid cylces
        dfs


        '''

        seen = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0


        def dfs(r, c):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1:
                return 
            if grid[r][c] == '0' or (r,c) in seen:
                return
            
            seen.add((r, c))

            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r - 1, c)





        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    dfs(r, c)
                    islands += 1
                    

        
        return islands