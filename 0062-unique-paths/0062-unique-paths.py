from math import factorial
class Solution:
    def uniquePaths(self, m, n):
        #the robot can only move in two directions either right or down 
        #initialise the first row and first column with 1
        dp = [[1] * n for _ in range(m)]
        #loop from second row and second column
        for x in range(1,m):
            for j in range(1,n):
                dp[x][j] = dp[x][j-1] + dp[x-1][j]
        return dp[m-1][n-1]
            


