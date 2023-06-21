# from functools import lru_cache

# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         @lru_cache(maxsize=None)
#         def helper(i, j):
#             if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]):
#                 return 0
#             if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
#                 return 1 - obstacleGrid[i][j]
#             if obstacleGrid[i][j] == 1:
#                 return 0
#             return helper(i + 1, j) + helper(i, j + 1)
        
#         return helper(0, 0)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Create a 2D dp array with the same dimensions as the grid
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first cell
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        # Fill the first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # Fill the first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the result stored in the bottom-right cell of the dp array
        return dp[m-1][n-1]