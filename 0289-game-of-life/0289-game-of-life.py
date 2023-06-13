class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #orignal new state
         # 0.       0.   0
         # 1        0.   1
         # 0        1    2
         # 1        1.   3
        row , col = len(board) , len(board[0])
        def checklife(r,c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            neig = 0
            for a in directions:
                if(0 <= (r + a[0]) <= (row- 1)) and (0 <= (c + a[1]) <= (col - 1)):
                    if board[r+a[0]][c+a[1]] in [1,3]:
                        neig+=1
            return neig
        for i in range(0,row):
            for j in range(0,col):
                neigh = checklife(i,j)
                if board[i][j]:
                    if neigh in [2,3]:
                        board[i][j] = 3
                elif neigh==3:
                    board[i][j]= 2
        for i in range(0,row):
            for j in range(0,col):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2,3]:
                    board[i][j] = 1
        
                    
        
        
                    