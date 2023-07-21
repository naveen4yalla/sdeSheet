from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        maxi = float('-inf')  # Initialize to negative infinity
        temp = 0
        for i in range(len(nums)):
            temp = max(nums[i], temp + nums[i])
            maxi = max(temp, maxi)
            
        return maxi
        
        