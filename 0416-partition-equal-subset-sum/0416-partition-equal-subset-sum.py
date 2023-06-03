class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dp(index,target):
            if target == 0:
                return True
            if index==0 or target <0:
                return False
            return dp(index-1,target-nums[index-1]) or dp(index-1,target)
        totalSum = sum(nums)
        if totalSum%2 != 0:
            return False
        return dp(len(nums)-1 , totalSum//2)
