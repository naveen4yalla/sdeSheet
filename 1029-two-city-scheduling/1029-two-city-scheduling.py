class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        memo = {}
        
        def dp(i, a_count, b_count):
            if i == 2 * n:
                if a_count == n and b_count == n:
                    return 0
                return float('inf')
            if (i, a_count, b_count) in memo:
                return memo[(i, a_count, b_count)]
            
            cost_a = costs[i][0] + dp(i + 1, a_count + 1, b_count)
            cost_b = costs[i][1] + dp(i + 1, a_count, b_count + 1)
            
            memo[(i, a_count, b_count)] = min(cost_a, cost_b)
            return memo[(i, a_count, b_count)]
        
        return dp(0, 0, 0)