# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total_sum = sum(nums)

#         # If the total sum is odd, it's impossible to partition the array into two equal-sum subsets.
#         if total_sum % 2 != 0:
#             return False

#         target_sum = total_sum // 2
#         memo = {}

#         def dfs(i, current_sum):
#             if current_sum == target_sum:
#                 return True

#             if i == len(nums) or current_sum > target_sum:
#                 return False

#             if (i, current_sum) in memo:
#                 return memo[(i, current_sum)]

#             # Try including the current element in the subset.
#             if dfs(i + 1, current_sum + nums[i]):
#                 memo[(i, current_sum)] = True
#                 return True

#             # Try excluding the current element from the subset.
#             if dfs(i + 1, current_sum):
#                 memo[(i, current_sum)] = True
#                 return True

#             memo[(i, current_sum)] = False
#             return False

#         return dfs(0, 0)
from functools import lru_cache
class Solution:
    def canPartition(self, nums):
        @lru_cache(maxsize=None)
        def dfs(nums, n, subset_sum):
            # Base cases
            if subset_sum == 0:
                return True
            if n <=-1 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)