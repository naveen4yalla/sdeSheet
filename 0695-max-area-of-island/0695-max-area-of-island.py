class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        result = 0
        
        def isInvalid(r, c):
            return r >= rows or r < 0 or c >= cols or c < 0
        
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def dfs(r, c):
            if isInvalid(r, c) or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            res = 0
            for i, j in directions:
                res = res + dfs(r + i, c + j)
            return res+1
        
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))
        
        return result
        