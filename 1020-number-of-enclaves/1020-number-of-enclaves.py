class Solution:
    def numEnclaves(self, grid):
        m = len(grid)
        n = len(grid[0])
        count =[0]
        def dfs(i,j, isBoundary):
            if i < 0 or i >= m or j < 0 or j>= n or grid[i][j]!=1 or (i,j) in visited:
                return
            
            visited.add((i,j))
            if not isBoundary:
                count[0] = count[0] + 1
            for x,y in [(0,-1), (0,1), (-1,0), (1,0)]:
                dfs(i+x, j+y, isBoundary)
        visited = set()
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0,j,True)
            if grid[m-1][j] == 1:
                dfs(m-1,j,True)
        for j in range(m):
            if grid[j][0] == 1 and (j,0) not in visited:
                dfs(j,0,True)
            if grid[j][n-1] == 1 and (j,n-1) not in visited:
                dfs(j,n-1,True)
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == 1 and (i,j) not in visited:
                     dfs(i,j,False)
        return count[0]

        
        
# s = Solution()
# s.numEnclaves([[0],[1],[1],[0],[0]])