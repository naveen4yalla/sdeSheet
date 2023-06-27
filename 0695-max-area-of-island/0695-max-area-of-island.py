from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        result = 0
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def isInvalid(r, c):
            return r >= rows or r < 0 or c >= cols or c < 0
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = 0
                    stack = [(i, j)]
                    while stack:
                        r, c = stack.pop()
                        if (r, c) not in visited and grid[r][c] == 1:
                            visited.add((r, c))
                            area += 1
                            for dr, dc in directions:
                                nr, nc = r + dr, c + dc
                                if not isInvalid(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 1:
                                    stack.append((nr, nc))
                    result = max(result, area)
        
        return result
        