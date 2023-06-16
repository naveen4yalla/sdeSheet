from functools import lru_cache
# class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     @lru_cache(None)
    #     def rob_helper(i):
    #         if i>=len(nums):
    #             return 0
    #         ans = max(rob_helper(i+1),rob_helper(i+2)+nums[i])
    #         return ans
    #     return rob_helper(0)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # arr = []
        # if nums == []:
        #     return 0
        # arr.append(0)
        # arr.append(nums[0])
        # for i in range(2,len(nums)+1):
        #     arr.append( max(arr[i-1],arr[i-2]+nums[i-1]))
        # return arr[-1]
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1
    
        