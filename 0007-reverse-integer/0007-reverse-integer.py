class Solution:
    def reverse(self, x: int) -> int:
        #check whether the number is negative or positive
        sign = 1
        result = 0
        if x < 0:
            sign = -1
            x = abs(x)
        while x!=0:
            pop = x % 10
            x= x//10
            result = result * 10 + pop
        result = result * sign
        if result < -2**31 or result > 2**31 - 1:
            return 0
        else:
            return result
            
        