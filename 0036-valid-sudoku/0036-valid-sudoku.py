class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_dict = {i:set() for i in range(9)}
        col_dict = {i:set() for i in range (9)}
        sub_dict = {i:set() for i in range(9)}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_dict[i] :
                        return False
                    row_dict[i].add(board[i][j])
                    if board[i][j] in col_dict[j]:
                        return False
                    col_dict[j].add(board[i][j])
                    sub = 3 * (i//3) + (j//3)
                    if board[i][j] in sub_dict[sub]:
                        return False
                    sub_dict[sub].add(board[i][j])
        return True
                    
        
        