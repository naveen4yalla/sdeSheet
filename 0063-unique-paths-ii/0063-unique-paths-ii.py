from functools import lru_cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def helper(i, j):
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]):
                return 0
            if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                return 1 - obstacleGrid[i][j]
            if obstacleGrid[i][j] == 1:
                return 0
            return helper(i + 1, j) + helper(i, j + 1)
        
        return helper(0, 0)