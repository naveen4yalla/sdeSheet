# class Solution:
#     def rearrangeSticks(self, n: int, k: int) -> int:
#         # dp = {}
#         @lru_cache(maxsize=None)
#         def helper(n,k):
#             if n== 0 or k == 0:
#                 return 0
#             if n==k: return 1
            
#             # if (n,k) in dp:
#             #     return dp[(n,k)]
#             # dp[(n,k)] = helper(n-1,k-1) + (n-1) * helper(n-1,k)
#             # return dp[(n,k)]
#             return helper(n-1,k-1) + (n-1) * helper(n-1,k)
#         return helper(n,k) % ((10**9) + 7)

class Solution:
    def rearrangeSticks(self,n,k):
        dp = {(1,1) : 1}
        for i in range(2,n+1):
            for j in range(1,k+1):
                dp[(i,j)] = dp.get((i-1,j-1),0) + (i-1) * dp.get((i-1,j),0)
        return dp[(i,j)] % ((10**9) + 7)
                