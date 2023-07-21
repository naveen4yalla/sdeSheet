class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #keep track of the total 
        total = 0
        currMin = 0
        currMax = 0
        globalmin = float("inf")
        globalmax = float("-inf")
        
        for i in nums:
            total+=i
            currMax = max(i,currMax+i)
            currMin = min(i,currMin + i)
            globalmin = min(globalmin,currMin)
            globalmax = max(globalmax,currMax)
        
        return max(globalmax, total - globalmin) if globalmax > 0 else globalmax
            
        