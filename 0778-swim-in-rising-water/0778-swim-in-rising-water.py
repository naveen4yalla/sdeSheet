import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        seen = {(0, 0)}
        waterLevel = [(grid[0][0], 0, 0)]
        depth = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Fixed directions

        while waterLevel:
            d, row, column = heapq.heappop(waterLevel)
            depth = max(depth, d)
            if row == column == N - 1:
                return depth

            for r, c in directions:
                new_row, new_column = row + r, column + c
                if checkBoundary(new_row, new_column, N) and (new_row, new_column) not in seen:  # Fixed condition
                    heapq.heappush(waterLevel, (grid[new_row][new_column], new_row, new_column))
                    seen.add((new_row, new_column))

        return -1  # If no valid path is found

def checkBoundary(r, c, N):
    if 0 <= r < N and 0 <= c < N:  # Fixed boundary check
        return True
    return False
