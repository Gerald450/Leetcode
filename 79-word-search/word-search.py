class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        input: grid, word
        output: boolean if word in grid

        edge: ascii, empty str, empty grid

        plan:
        graph traversal
        dfs 
        use used set
        if i find first letter, look at adj letters not in used
        keep looking and following different paths until i is equal to length of word
        if i is equal to length of word, return True
        if not return False
        '''
        used = set()
        rows, cols = len(board), len(board[0])

        def dfs(i, row_idx, col_idx):
            if i == len(word):
                return True

            if ((row_idx not in range(0, rows) or 
                col_idx not in range(0, cols)) or
                i not in range(len(word)) or
                word[i] != board[row_idx][col_idx] or
                (row_idx, col_idx) in used):
                return False
            

            used.add((row_idx, col_idx))
            
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            
            for dr in directions:
                r, c = dr
                row, col = row_idx + r, col_idx + c
                if dfs(i + 1, row, col):
                    return True

            used.discard((row_idx, col_idx))
            return False

        
        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True

        return False





            


        