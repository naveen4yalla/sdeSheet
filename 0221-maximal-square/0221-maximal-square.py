class Solution:
    def maximalSquare(self, mat):
        if not mat or not len(mat):
            return 0
        T = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
        maxvalue = 0

        # fill in a bottom-up manner
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                T[i][j] = int(mat[i][j])

                # if we are not at the first row or first column and the
                # current cell has value 1
                if i > 0 and j > 0 and mat[i][j] == "1":
                    # the largest square submatrix ending at `mat[i][j]` will be 1 plus
                    # minimum of the largest square submatrix ending at `mat[i][j-1]`,
                    # `mat[i-1][j]` and `mat[i-1][j-1]`

                    T[i][j] = min(T[i][j - 1], T[i - 1][j], T[i - 1][j - 1]) + 1

                # update maximum size found so far
                if maxvalue < T[i][j]:
                    maxvalue = T[i][j]

        # return size of the largest square matrix
        return maxvalue ** 2
#         directions = [(0,1),(1,0),(1,1)]
#         m , n = len(matrix),len(matrix[0])
#         @lru_cache(maxsize=128)
#         def maxSquareHelper(i,j,size,maxSize):
            
#             if i<=m-1 and j<=n-1 and i>=0 and j>=0:
                
#                 left,maxSize = maxSquareHelper(i+0,j+1,size,maxSize)
#                 down,maxSize= maxSquareHelper(i+1,j+0,size,maxSize)
#                 diagonal,maxSize = maxSquareHelper(i+1,j+1,size,maxSize)
#                 if matrix[i][j] == "0":
#                     size = 0
#                 else:
#                     size = 1 + min(left,down,diagonal)
#                 return size,max(size,maxSize)
#             else:
#                 return 0,maxSize
        
#         size , maxSize = maxSquareHelper(0,0,0,0)
#         return maxSize ** 2
          