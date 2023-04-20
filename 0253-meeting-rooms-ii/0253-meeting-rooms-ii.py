class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[0])
        minheap =[]
        heapq.heappush(minheap,intervals[0][1])
        for i,j in intervals[1:]:
            if minheap[0] <= i:
                heapq.heappop(minheap)
            heapq.heappush(minheap,j)
            
        return len(minheap)
                