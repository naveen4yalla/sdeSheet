class Solution:
    def longestSubarray(self, nums):
        left = 0
        count = 1
        right = 0
        result = 0
        while right < len(nums):
            if nums[right] == 0:
                count-=1
            while count==-1:
                if nums[left] is 0:
                    count+=1
                left += 1
            
            result = max(result , right-left)
            right+=1
        return result
    
        