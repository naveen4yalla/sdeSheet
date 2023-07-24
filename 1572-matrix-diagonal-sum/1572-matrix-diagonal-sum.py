class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row  = len(mat)
        cols = len(mat[0])
        p = 0
        s = 0
        
        for i in range(row):
            p = p + mat[i][i]
            s = s + mat[i][row - i - 1]
        if row % 2:
            return  p + s - mat[row//2][cols//2]
        else:
            return p + s