# from typing import List

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         memo = [None] * n
        
#         def can_reach_last(index):
#             if index == n - 1:  # If we reach the last index, return True
#                 return True
            
#             if memo[index] is not None:  # If the result for this index is already calculated, return it
#                 return memo[index]
            
#             furthest_jump = min(index + nums[index], n - 1)  # Calculate the furthest jump from this index
#             for j in range(index + 1, furthest_jump + 1):
#                 if can_reach_last(j):
#                     memo[index] = True  # If we can reach the last index from index j, we can also reach it from this index
#                     return True
            
#             memo[index] = False  # If we can't reach the last index from any index reachable from this index, return False
#             return False
        
#         return can_reach_last(0)
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
