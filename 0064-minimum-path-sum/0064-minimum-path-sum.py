class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # Create a 2D dp array with the same dimensions as the grid
        dp = [[0] * n for _ in range(m)]
        
        # Iterate over each cell in the grid
        for i in range(m):
            for j in range(n):
                # Base case: if it's the top-left cell, set dp[i][j] to grid[i][j]
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                # For cells in the first row, only consider the path from the left cell
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                # For cells in the first column, only consider the path from the top cell
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                # For other cells, choose the minimum path from the top and left cells
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        # Return the minimum path sum stored in the bottom-right cell of dp
        return dp[m-1][n-1]

        
