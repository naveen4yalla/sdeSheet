# from functools import lru_cache
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         #optimise the performance
#         nums.sort()
        
#         @lru_cache(maxsize = None)
#         def combinations(remain):
#             if remain == 0:
#                 return 1
#             result = 0
#             for num in nums:
#                 if remain - num >= 0:
#                     result += combinations(remain - num)
#                 else:
#                     break
#             return result 
#         return combinations(target)
from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # minor optimization
        # nums.sort()
        dp = [0 for i in range(target+1)]
        dp[0] = 1

        for comb_sum in range(target+1):

            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum-num]
                # minor optimization, early stopping.
                # else:
                #    break
        return dp[target]
    