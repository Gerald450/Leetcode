class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        '''
        BFS Graph traversal
        reverse board
        create a helper for pos to cordinate conversion
        store pos and moves in deque
        '''
        n = len(board)

        def PosToCord(num):
            row = (num - 1) // n
            col = (num - 1) % n
            if row % 2:
                col = n - 1 - col
            row = n - 1 - row
            return (row, col)

        q = deque([(1, 0)]) #pos, moves
        seen = set()

        while q:
            pos, moves = q.popleft()
            for i in range(1, 7): #simulate dice row
                newPos = pos + i
                r,c = PosToCord(newPos)
                if board[r][c] != -1:
                    newPos = board[r][c]
                if newPos not in seen:
                    seen.add(newPos)
                    q.append((newPos, moves + 1))
                if newPos == pow(n, 2):
                    return moves + 1
                
        return -1


        '''
        runtime: O(n^2)
        space:O(n^2)
        '''

       

        


        

        