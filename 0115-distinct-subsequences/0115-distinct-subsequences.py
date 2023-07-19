class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # Create a 2D DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the base cases
        for i in range(m + 1):
            dp[i][n] = 1
        
        # Fill the DP table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]  # Consider excluding current character
                
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]  # Consider including current character
        
        return dp[0][0]