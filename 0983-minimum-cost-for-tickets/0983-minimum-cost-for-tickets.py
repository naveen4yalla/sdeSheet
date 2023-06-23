from typing import List
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1, 7, 30]  # Durations corresponding to the pass types
        
        @lru_cache(None)
        def helper(index):
            if index >= len(days):
                return 0
            
            result = float('inf')
            for i, cost in enumerate(costs):
                j = index
                while j < len(days) and days[j] < days[index] + durations[i]:
                    j += 1
                result = min(result, cost + helper(j))
            
            return result
        
        return helper(0)
