
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        # to store previously computed values in the dp array
        dp = {}
        # traverse in all four directions
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def isInvalid(r, c):
            return r >= rows or r < 0 or c >= cols or c < 0
        
        def dfs(r, c, prevVal):
            if isInvalid(r, c) or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            result = 0
            for i, j in directions:
                result = max(result, dfs(r + i, c + j, matrix[r][c]) + 1)
            dp[(r, c)] = result
            return result
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, -1)
        
        return max(dp.values(), default=0)
            
            
            
        
        