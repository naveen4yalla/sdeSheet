class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        rows, cols = len(grid2), len(grid2[0])  # Use grid2 instead of grid
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or (r, c) in visit
                or grid2[r][c] == 0
            ):
                return True

            visit.add((r, c))
            res = True
            if grid1[r][c] == 0:  # Use grid1 instead of grid
                res = False
            res &= dfs(r - 1, c)
            res &= dfs(r + 1, c)
            res &= dfs(r, c - 1)
            res &= dfs(r, c + 1)
            return res

        for f in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[f][j] and (f, j) not in visit and dfs(f, j):
                    count += 1
        return count
        