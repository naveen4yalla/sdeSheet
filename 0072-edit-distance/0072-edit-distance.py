from functools import lru_cache

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         @lru_cache(maxsize=None)
#         def helper(i, j):
#             if i >= len(word1):
#                 return len(word2) - j 
#             if j >= len(word2):
#                 return len(word1) - i

#             if word1[i] == word2[j]:
#                 return helper(i + 1, j + 1)
#             else:
#                 return min(helper(i, j + 1) + 1, helper(i + 1, j) + 1, helper(i + 1, j + 1) + 1)

#         return helper(0, 0)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]
            
                
                
        