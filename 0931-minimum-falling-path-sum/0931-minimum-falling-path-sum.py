from functools import lru_cache
        
class Solution:
     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
            dp = [[0] * len(matrix[0]) for f in range(len(matrix))]
            for i in range(0,len(matrix[0])):
                dp[0][i] = matrix[0][i]
            for i in range(1,len(matrix)):
                for j in range(len(matrix[0])):
                    if j == 0:
                        dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])
                    elif j == len(matrix[0])-1:
                        dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j -1])
                    else:
                        dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j -1],dp[i-1][j+1])
            mine = float("inf")
            for i in range(0,len(matrix[0])):
                mine = min(mine,dp[len(matrix[0])-1][i])
            return mine
                
                                                                            
                        
#         sum = 100000
#         @lru_cache(maxsize=None)
#         def minutil(i,j):
#             if 0 <= j < len(matrix) or 0 <= j < len(matrix[0]):
#                 if i==len(matrix)-1:
#                     return matrix[i][j]
#                 diagonal = min(minutil(i+1,j-1),minutil(i+1,j+1))
#                 right = min(minutil(i+1,j),diagonal)
#                 return matrix[i][j] + right
#             else:
#                 return 100000
            
#         for f in range(0,len(matrix[0])):
#             sum = min(minutil(0,f) ,sum)
#         return sum 

         
