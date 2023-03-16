from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @lru_cache(None)
        def backTrack(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_cost = float("inf")
            for c in coins :
                result = backTrack(rem - c)
                if result != -1:
                    min_cost = min(min_cost,result + 1)
            return min_cost if min_cost != float("inf") else -1


        
        return backTrack(amount)