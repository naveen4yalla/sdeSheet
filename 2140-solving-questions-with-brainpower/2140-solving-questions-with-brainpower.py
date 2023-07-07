class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        n = len(questions)
        
        def dfs(q):
            if q >= n:
                return 0
            if q in dp:
                return dp[q]
            p, s = questions[q]
            dp[q] = max(dfs(q + 1), p + dfs(q + s + 1))
            return dp[q]

        return dfs(0)
