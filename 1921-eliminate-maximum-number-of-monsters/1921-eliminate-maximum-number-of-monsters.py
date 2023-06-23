# class Solution:
#     def eliminateMaximum(self,dist, speed):
#         time = 0
#         monsters = [(dist[i] / speed[i]) for i in range(len(dist))]
#         heapq.heapify(monsters)
#         while monsters:
#             if time >= heapq.heappop(monsters):
#                 return time
#             time = time + 1
#         return time
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        n = len(dist)                                                       
        time = sorted(map(lambda x: int(ceil(x[0]/x[1])),zip(dist,speed))) 
                                                                                 
        for i in range(n):                                                                
            if i >= time[i]: return i                                                 
                                                                                       
        return n                                                                                       
        

        
        