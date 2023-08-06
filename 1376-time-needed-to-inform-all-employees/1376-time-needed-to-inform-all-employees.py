from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        #create a adjancy list
        ds = defaultdict(list)
        for i in range(n):
            ds[manager[i]].append(i)
        queue = [(headID,informTime[headID])]
        maxTime = 0
        while queue:
            id , time = queue.pop(0)
            maxTime = max(time,maxTime)
            
            
            #iterate on ther list
            for i in ds[id]:
                queue.append((i,time+informTime[i]))
        return maxTime
            