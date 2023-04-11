from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def rob_helper(i):
            if i>=len(nums):
                return 0
            ans = max(rob_helper(i+1),rob_helper(i+2)+nums[i])
            return ans
        return rob_helper(0)
    
        