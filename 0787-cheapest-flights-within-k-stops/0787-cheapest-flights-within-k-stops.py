from collections import defaultdict,deque
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph= defaultdict(list)
        for v1,v2,cost in flights:
            graph[v1].append([v2,cost])
        seen =set()
        distance={src:0}
        q=[]
        q.append([0,src,0])
        while q:
            front = q.pop(0)
            stops = front[0]
            node = front[1]
            cost = front[2]
            if stops > k:
                continue
            for f in graph[node]:
                
                if cost + f[1] < distance.get(f[0],float('inf')) and stops  <= k:
                    distance[f[0]] = cost + f[1]
                    q.append([stops+1,f[0],cost + f[1]])
        if distance.get(dst,float('inf')) == float('inf'):
            return -1
        return distance[dst]

            
            
        
        