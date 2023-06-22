class Solution:
    def change(self,amount,coins):
        memo = {}
        @lru_cache(None)
        def dp(amount, index):
            # Check if the solution has already been memoized
            if (amount, index) in memo:
                return memo[(amount, index)]

            # Base cases
            if amount == 0:
                return 1
            if amount < 0 or index >= len(coins):
                return 0

            # Recurse with the current coin or move to the next coin
            combinations = dp(amount - coins[index], index) + dp(amount, index + 1)
            return combinations

        return dp(amount, 0)

            
        