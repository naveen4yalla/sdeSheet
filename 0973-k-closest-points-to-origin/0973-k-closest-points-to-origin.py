class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if points == 1:return points
        ls = []
        heapq.heapify(ls)
        result = []
        for a , b in points:
            value = abs(a * a + b * b)
            heapq.heappush(ls,[value,(a,b)])
        for i in range(0,k):
            _,temp = heapq.heappop(ls)
            result.append(temp)
        return result
            