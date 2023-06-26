class Solution:

    def snakesAndLadders(self,board):
        n = len(board)
        target = n * n

        queue = deque([(1, 0)])
        visited = set([1])
        def getRowCol(square, n):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col
         
        while queue:
            square, moves = queue.popleft()

            for i in range(1, 7):
                next_square = square + i

                if next_square > target:
                    break

                row, col = getRowCol(next_square, n)
                if board[row][col] != -1:
                    next_square = board[row][col]

                if next_square == target:
                    return moves + 1

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1

    

