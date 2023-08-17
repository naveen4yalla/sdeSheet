from collections import defaultdict
import heapq
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ls = defaultdict(list)
        for  i , j , d in roads:
            ls[i].append([j,d])
            ls[j].append([i,d])
        queue = [1]
        visited = set()
        result = float("inf")
        while queue:
            node = queue.pop(0)
            for i , d in ls[node]:
                result = min(d,result)
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return result
            