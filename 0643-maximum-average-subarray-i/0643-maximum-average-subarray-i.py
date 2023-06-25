class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_average = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_average = max(max_average, window_sum)

        return max_average/k

                
        
            
        