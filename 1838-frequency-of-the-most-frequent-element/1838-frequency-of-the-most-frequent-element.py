class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total,left,right = 0 , 0 , 0
        result = 0
        while right < len(nums):
            total += nums[right]
            while (right - left + 1)*nums[right] >total + k:
                total -= nums[left]
                left = left +1
            result = max(result , right-left +1)
            right = right +1
        return result
            
                