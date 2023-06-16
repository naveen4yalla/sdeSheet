class Solution:
    def maxProduct(self, nums: List[float]) -> float:
        if len(nums) == 0:
            return 0
        #initialise the min and max to the start 
        max_so_far = nums[0]
        min_so_far = nums[0]
        #currently the result is at max_So_far
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            #capture the maximum  
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            #capture the minimum 
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result