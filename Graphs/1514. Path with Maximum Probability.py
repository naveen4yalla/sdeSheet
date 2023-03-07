from collections import defaultdict
from heapq import *
class Solution:
    def maxProbability(self, n, edges , succProb, start, end):
        graph = defaultdict(list)
        #create a graph
        for i in range(len(edges)):
            graph[edges[i][0]].append((-succProb[i],edges[i][1]))
            graph[edges[i][1]].append((-succProb[i],edges[i][0]))
        seen = set()
        distance = {start : -1}
        queue = [(-1,start)]
        while queue:
            cost,v1=heappop(queue)
            if v1 not in seen:
                seen.add(v1)
                if v1==end:
                    return -cost 
            for profit ,v2 in graph.get(v1,()):
                if v2 in seen:
                    continue
                prev = distance.get(v2,None)
                next = cost * profit * -1
                if prev is None or next < prev:
                    distance[v2] = next
                    heappush(queue,(next,v2))
        return 0.00000
