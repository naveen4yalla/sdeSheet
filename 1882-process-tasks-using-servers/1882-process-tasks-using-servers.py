import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        #use two min-heaps to solve the problem 
        result = [0] * len(tasks)
        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)
        notAvailable = []
        heapq.heapify(notAvailable)
        t = 0
        for f in range(len(tasks)):
            t = max(t, f)
            if len(available) == 0:
                t = notAvailable[0][0]
            while notAvailable and t >= notAvailable[0][0]:
                time, weight, index = heapq.heappop(notAvailable)
                heapq.heappush(available, (weight, index))
            weight, index = heapq.heappop(available)
            result[f] = index
            heapq.heappush(notAvailable, (t + tasks[f], weight, index))
        return result
            
                