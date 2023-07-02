
from typing import List


       
     
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    queue.append([i, j])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def isInvalid(r, c):
            return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])
        
        r = -1
        if (len(queue) == 0) | (len(queue) == len(grid)*len(grid[0])):
            return -1
        while queue:
            a, b = queue.pop(0)
            r = grid[a][b]
            for i, j in directions:
                newr, newc = a + i, b + j
                if not isInvalid(newr, newc) and grid[newr][newc] == 0:
                    queue.append([newr, newc])
                    grid[newr][newc] = grid[a][b] + 1
        
        return r-1 if r != -1 else -1          
            
            