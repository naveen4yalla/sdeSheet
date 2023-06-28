#import heapq

class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, -num)
        if self.minHeap and self.maxHeap and -self.minHeap[0] > self.maxHeap[0]:
            val = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-(self.minHeap[0]) + self.maxHeap[0]) / 2.0
        if len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        return self.maxHeap[0]
    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()