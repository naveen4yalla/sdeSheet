class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        rows = len(matrix)
        cols = len(matrix[0])
        atlantic = set()
        pacific = set()
        def isInvalid(r,c):
            return r<0 or c< 0 or r>=rows or c>=cols
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(r,c,visited,value):
            if isInvalid(r,c) or (r,c) in visited or matrix[r][c] < value:
                return 
            visited.add((r,c))
            for i,j in directions:
                dfs(r+i,c+j,visited,matrix[r][c])
        for c in range(cols):
            dfs(0,c,pacific,matrix[0][c])
            dfs(rows-1,c,atlantic,matrix[rows-1][c])
        for r in range(rows):
            dfs(r,0,pacific,matrix[r][0])
            dfs(r,cols-1,atlantic,matrix[r][cols-1])
        result = []
        for i in range(rows):
            for c in range(cols):
                if (i,c) in pacific and (i,c) in atlantic:
                    result.append([i,c])
        return result
            