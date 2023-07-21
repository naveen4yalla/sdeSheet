import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = {}
        for i in hand:
            counter[i] = counter.get(i, 0) + 1
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            minValue = minHeap[0]
            for i in range(minValue, minValue + groupSize):
                if i not in counter:  # Corrected variable name here
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i!= minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
