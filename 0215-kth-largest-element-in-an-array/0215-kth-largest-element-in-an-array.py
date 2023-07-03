import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ls = []
        heapq.heapify(ls)
        for f in range(0, len(nums)):
            ls.append(-nums[f])
        return -heapq.nsmallest(k, ls)[-1]
                