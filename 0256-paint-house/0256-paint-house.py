class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red, blue, green = 0, 0, 0
        for cr, cb, cg in costs:
            red, blue, green = min(blue, green) + cr, min(red, green) + cb, min(red, blue) + cg
        return min(red, blue, green)
        