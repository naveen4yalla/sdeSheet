class Solution:
    def eliminateMaximum(self,dist, speed):
        time = 0
        monsters = [(dist[i] / speed[i]) for i in range(len(dist))]
        heapq.heapify(monsters)
        while monsters:
            if time >= heapq.heappop(monsters):
                return time
            time = time + 1
        return time
                
        

        
        