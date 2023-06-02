class Solution:
    def rotate(self,matrix):
        left , right = 0 , len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top , bottom = left , right
                #save the top-left 
                topleft = matrix[top][left+i]
                #move bottom left to top left
                matrix[top][left+i] = matrix[bottom-i][left]
                #move bottom right into bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                #move top right  into bottom right
                matrix[bottom][right-i] = matrix[top+i][right]
                #save the temp into topleft
                matrix[top+i][right] = topleft
            left+=1
            right-=1
                  
                
            