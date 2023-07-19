class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumofall = sum(stones)
        halfSum = ceil(sumofall/2)
        n = len(stones)
        @lru_cache(maxsize=None)
        def dfs(i,total):
            if total>=halfSum or i == n:
                return abs(total-(sumofall-total))
            
            return min(dfs(i+1,total+stones[i]),dfs(i+1,total))
        return dfs(0,0)
        