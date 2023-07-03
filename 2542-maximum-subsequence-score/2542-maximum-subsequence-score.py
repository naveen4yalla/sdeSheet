class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        mapList = [(i,j) for i , j in zip(nums1,nums2)]
        mapList = sorted(mapList,key=lambda p: p[1],reverse=True)
        sumOfnums1 = 0
        minHeap = []
        result = 0
        for i , j in mapList:
            sumOfnums1+=i
            heapq.heappush(minHeap,i)
            if k < len(minHeap):
                sumOfnums1 = sumOfnums1 - heapq.heappop(minHeap)
                
            if k == len(minHeap):
                result = max(result,j * sumOfnums1) 
        return result
        