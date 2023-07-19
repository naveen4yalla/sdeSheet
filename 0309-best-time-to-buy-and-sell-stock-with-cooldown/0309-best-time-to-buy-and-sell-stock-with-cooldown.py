class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i,buying):
            if i>=len(prices):
                return 0
            cooldown = dfs(i+1,buying)
            if buying:
                return max(cooldown,dfs(i+1,not buying)-prices[i])
            else:
                return max(cooldown,dfs(i+2,not buying)+prices[i])
            
        return dfs(0,True)
        