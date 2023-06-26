from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()

        def isInvalid(r, c):
            return r < 0 or c < 0 or r == n or c == n

        def dfs(r, c):
            if isInvalid(r, c) or (r, c) in visited or grid[r][c] != 1:
                return
            visited.add((r, c))
            for i, j in directions:
                dfs(r + i, c + j)

        def bfs():
            queue = deque(visited)
            distance = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    r, c = queue.popleft()
                    for i, j in directions:
                        ra, rb = r + i, c + j
                        if isInvalid(ra, rb) or (ra, rb) in visited:
                            continue
                        if grid[ra][rb] == 1:
                            return distance
                        queue.append((ra, rb))
                        visited.add((ra, rb))
                distance += 1
            return -1  # If no bridge is found

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()

                