class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        memo = {}

        def helper(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            take_one_step = cost[i] + helper(i + 1)
            take_two_steps = cost[i] + helper(i + 2)

            memo[i] = min(take_one_step, take_two_steps)
            return memo[i]

        return min(helper(0), helper(1))

        