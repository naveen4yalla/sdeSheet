class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #Add the index to the end opf the list 
        for i,j in enumerate(tasks):
            j.append(i)
        #sort the tasks according to ther to their enqueTimes
        tasks.sort(key= lambda t:t[0])
        result ,minHeap = [] , []
        time = tasks[0][0]
        i= 0
        while i<len(tasks) or minHeap:
            while i < len(tasks) and time >=tasks[i][0]:
                heapq.heappush(minHeap,(tasks[i][1],tasks[i][2]))
                i+=1
            if minHeap:
                processTime , index = heapq.heappop(minHeap)
                result.append(index)
                time = processTime + time
            else:
                time = tasks[i][0]
        return result
                           