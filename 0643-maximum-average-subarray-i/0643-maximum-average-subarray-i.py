class Solution:
    def findMaxAverage(self, nums, k):
        total_sum = 0
        right = 0
        maxtotal = 0
        if len(nums) == k:
            return sum(nums) / k
        while right < len(nums):
                    if right < k:
                        total_sum = total_sum + nums[right]
                        maxtotal = total_sum
                    else:
                        total_sum = total_sum-nums[right-k]+nums[right]
                        maxtotal = max(total_sum,maxtotal)
                    right+=1
        return maxtotal/k
                
        
            
        