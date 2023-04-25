class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        result = [0]
        offset  = 1
        for f in range(1,n+1):
            if offset * 2 == f:
                offset = f
            dp[f] =  1 + dp[f-offset]
        return dp
        