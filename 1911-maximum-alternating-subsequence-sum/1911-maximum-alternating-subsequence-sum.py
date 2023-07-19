class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        include_sum = nums[0]  # Maximum alternating sum ending at index i, considering the last element included
        exclude_sum = 0  # Maximum alternating sum ending at index i, considering the last element excluded
        
        for i in range(1, len(nums)):
            new_include_sum = max(exclude_sum + nums[i], include_sum)  # Calculate the new include sum
            exclude_sum = max(include_sum - nums[i], exclude_sum)  # Calculate the new exclude sum
            
            include_sum = new_include_sum
        
        return include_sum  # Return the maximum alternating sum ending at the last index
