from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #create a graph from all points
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1 , y1 = points[i]
            for j in range(i+1,n):
                x2 , y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                graph[i].append([distance,j])
                graph[j].append([distance,i])
        minHeap = [[0,0]] # distance and node
        result = 0
        visited = set()
        while len(visited) < n:
            d , node = heapq.heappop(minHeap)
            if node  in visited:
                continue
            result+= d
            visited.add(node)
            for neiDistance , adjnode in graph[node]:
                heapq.heappush(minHeap,[neiDistance,adjnode])
            
        return result
            
        