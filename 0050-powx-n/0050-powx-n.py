#Time complexity is o(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:
                return 1
            res = helper(x*x ,n//2)
            return x * res if n%2 == 1 else res
        if x==0: return 0
        
        res = helper(x,abs(n))
        if n >=0:return res
        return 1/res
        

        