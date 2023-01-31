from functools import lru_cache
class Solution:
    def trianglePathSum(self,i,j,row,col,tri):
        if j == col:
            return 0
        if i == row-1:
            return tri[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = tri[i][j] + max(self.trianglePathSum(i+1,j,row,col,tri),self.trianglePathSum(i+1,j+1,row,col,tri))
        return dp[i][j]   
    def maxPathSum(self,tri, m, n):
 
    # loop for bottom-up calculation
        for i in range(m-1, -1, -1):
            for j in range(i+1):
    
                # for each element, check both
                # elements just below the number
                # and below right to the number
                # add the maximum of them to it
                if (tri[i+1][j] > tri[i+1][j+1]):
                    tri[i][j] += tri[i+1][j]
                else:
                    tri[i][j] += tri[i+1][j+1]
    
        # return the top element
        # which stores the maximum sum
        return tri[0][0]
    
N =3
tri = [ [1, 0, 0],
        [4, 8, 0],
        [1, 5, 3] ]
dp = [[-1 for i in range(N)]for j in range(N)]
s =Solution()
s.trianglePathSum(0,0,3,3,tri)