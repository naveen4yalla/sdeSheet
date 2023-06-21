class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        sum = 0
        a ,b = 0 ,1
        for f in range(2,n+1):
            sum = a + b
            a = b 
            b = sum 
        return sum
            
        