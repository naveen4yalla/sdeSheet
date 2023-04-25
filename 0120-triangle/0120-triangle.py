from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle):
        rows = len(triangle)
        result = 0 
        @lru_cache(None)
        def rec(i,j):
            if i==rows:
                return 0
            sum = 1000
            f = j+1
            for k in range(j,f+1):
                sum = min(rec(i+1,k)+triangle[i][j],sum) 
            
            result = sum 
            return result
        if rows==1:
            return triangle[0][0]
        return rec(0,0)
# s = Solution()
# s.minimumTotal([-10])
                
                
        