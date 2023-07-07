#It uses a recurive technique
# class Solution:
#     def mostPoints(self, questions: List[List[int]]) -> int:
#         dp = {}
#         n = len(questions)
        
#         def dfs(q):
#             if q >= n:
#                 return 0
#             if q in dp:
#                 return dp[q]
#             p, s = questions[q]
#             dp[q] = max(dfs(q + 1), p + dfs(q + s + 1))
#             return dp[q]

#         return dfs(0)
#Iterative approach 
class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * n
        dp[n - 1] = questions[n - 1][0]

        for i in range(n - 2, -1, -1):
            score = 0
            cool = questions[i][1]

            if cool + i + 1 >= n:
                score += questions[i][0]
            else:
                score += questions[i][0] + dp[i + cool + 1]

            dp[i] = max(score, dp[i + 1])

        return dp[0]


                
            
