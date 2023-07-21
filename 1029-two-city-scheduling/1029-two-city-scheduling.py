# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         n = len(costs) // 2
#         memo = {}
        
#         def dp(i, a_count, b_count):
#             if i == 2 * n:
#                 return 0
#             if (i, a_count, b_count) in memo:
#                 return memo[(i, a_count, b_count)]
            
#             cost_a = costs[i][0] + dp(i + 1, a_count + 1, b_count)
#             cost_b = costs[i][1] + dp(i + 1, a_count, b_count + 1)
            
#             if a_count == n:
#                 memo[(i, a_count, b_count)] = cost_b
#             else:
#                 memo[(i, a_count, b_count)] = min(cost_a, cost_b)
            
#             return memo[(i, a_count, b_count)]
        
#         return dp(0, 0, 0)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
        diffs.sort()
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs) / 2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]
        return res
