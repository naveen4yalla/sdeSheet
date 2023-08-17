class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        Rows = len(grid) 
        Cols = len(grid[0])
        visited =set()
        def dfs(i,j):
            if (i < 0 or j < 0 or i == Rows or j == Cols):
                return 0
            if grid[i][j] == 1 or (i,j) in visited:
                return 1
            visited.add((i,j))
            return min(
                dfs(i-1,j),
                dfs(i,j-1),
                dfs(i+1,j),
                dfs(i,j+1)
            )
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] != 1:
                    result = result + dfs(i,j)
        return result
            
        