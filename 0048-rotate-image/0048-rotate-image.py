class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return matrix
            
#     def rotate(self,matrix):
#         left , right = 0 , len(matrix) - 1
#         while left < right:
#             for i in range(right - left):
#                 top , bottom = left , right
#                 #save the top-left 
#                 topleft = matrix[top][left+i]
#                 #move bottom left to top left
#                 matrix[top][left+i] = matrix[bottom-i][left]
#                 #move bottom right into bottom left
#                 matrix[bottom-i][left] = matrix[bottom][right-i]
#                 #move top right  into bottom right
#                 matrix[bottom][right-i] = matrix[top+i][right]
#                 #save the temp into topleft
#                 matrix[top+i][right] = topleft
#             left+=1
#             right-=1
                    

            