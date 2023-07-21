from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}  # Memoization cache
        
        def dp(position):
            if position == n - 1:
                return 0  # Base case: We have already reached the last index
                
            if position in cache:
                return cache[position]  # Return the result from the cache if available
            
            min_jumps = float('inf')  # Initialize minimum jumps to a large value
            
            # Try all possible jumps from the current position
            for jump_length in range(1, nums[position] + 1):
                next_position = position + jump_length
                if next_position < n:
                    min_jumps = min(min_jumps, 1 + dp(next_position))
            
            cache[position] = min_jumps  # Store the result in the cache
            return min_jumps
        
        return dp(0)  # St