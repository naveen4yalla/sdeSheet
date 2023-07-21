# from typing import List

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return 0
        
#         queue = [(0, 0)]  # Initialize the queue with (index, jumps) tuple, starting from the first index
#         visited = set()  # Keep track of visited nodes
        
#         while queue:
#             index, jumps = queue.pop(0)  # Get the first element from the queue
#             visited.add(index)  # Mark the current node as visited
            
#             for jump_length in range(nums[index], 0, -1):
#                 next_index = index + jump_length
                
#                 if next_index >= n - 1:
#                     return jumps + 1
                
#                 if next_index not in visited:
#                     queue.append((next_index, jumps + 1))
        
#         return -1  # If the last index is not reachable, return -1
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res