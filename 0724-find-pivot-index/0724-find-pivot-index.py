class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot_sum = sum (nums)
        result = 0
        for i in range(len(nums)): 
            if result == tot_sum -result - nums[i]:
                return i
            else:
                result = result + nums[i]
        return -1      