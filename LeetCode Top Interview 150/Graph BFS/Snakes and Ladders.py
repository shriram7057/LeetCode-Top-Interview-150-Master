class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)

        def get_pos(sq):
            r = (sq - 1) // n
            c = (sq - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        from collections import deque
        q = deque([(1, 0)])
        visited = set([1])

        while q:
            sq, moves = q.popleft()
            if sq == n * n:
                return moves
            for step in range(1, 7):
                nxt = sq + step
                if nxt > n * n:
                    continue
                r, c = get_pos(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves + 1))
        return -1
