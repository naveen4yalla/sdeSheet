class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        heapq.heapify(maxHeap)
        if a!=0:heapq.heappush(maxHeap,[-a,'a'])
        if b!=0:heapq.heappush(maxHeap,[-b,'b'])
        if c!=0:heapq.heappush(maxHeap,[-c,'c'])
        result = ""
        while maxHeap:
            count ,char = heapq.heappop(maxHeap)
            if len(result) > 1 and result[-1] == char and result[-2] == char:
                if not maxHeap:
                    break
                count2,char2 = heapq.heappop(maxHeap)
                count2+=1
                result+=char2
                if count2:
                    heapq.heappush(maxHeap,[count2,char2])
            else:
                result+=char
                count+=1
            if count:
                heapq.heappush(maxHeap,[count,char])
        return result
                    