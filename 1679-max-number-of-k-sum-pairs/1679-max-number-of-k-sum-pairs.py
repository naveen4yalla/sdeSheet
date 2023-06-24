class Solution:
    def maxOperations(self, nums, k):
        left = 0
        right = len(nums) - 1
        count = 0
        nums.sort()
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                count+=1
                left+=1
                right-=1
            elif sum > k:
                right-=1
            else:
                left+=1
        return count
        