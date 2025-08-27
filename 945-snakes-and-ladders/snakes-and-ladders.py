class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        board.reverse()
        def helper(num):
            r = (num - 1) // n
            c = (num - 1) % n
            if r % 2 != 0:
                c = n - 1 - c
            return [r,c]

        q = deque()
        q.append([1, 0])
        seen = set()

        while q:
            pos, moves = q.popleft()
            for i in range(1, 7):
                newPos = pos + i
                r, c = helper(newPos)
                if board[r][c] != -1:
                    newPos = board[r][c]
                if newPos not in seen:
                    seen.add(newPos)
                    q.append([newPos, moves + 1])
                if newPos == pow(n, 2):
                    return moves + 1

        return -1
                
                

        