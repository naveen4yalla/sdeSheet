from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        dequearray = deque()
        output = []
        if k ==1:
            return nums
        
        for i in range(len(nums)):
            if dequearray and dequearray[0] == i-k:
                dequearray.popleft()
            while dequearray and dequearray[-1]<nums[i]:
                dequearray.pop()
            dequearray.append(i)
            if i>=k-1:
                output.append(nums[dequearray[0]])
        return output