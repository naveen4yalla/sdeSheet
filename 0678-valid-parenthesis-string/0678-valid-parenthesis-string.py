#Dynmaic Programming
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        n = len(s)
        
        def helper(index, count):
            if (index, count) in dp:
                return dp[(index, count)]
            if index == n:
                return count == 0
            if count < 0:
                return False
            
            if s[index] == '(':
                dp[(index, count)] = helper(index + 1, count + 1)
            elif s[index] == ')':
                dp[(index, count)] = helper(index + 1, count - 1)
            else:  # '*' can be treated as any of the three possibilities
                dp[(index, count)] = helper(index + 1, count + 1) or helper(index + 1, count) or helper(index + 1, count - 1)
            
            return dp[(index, count)]
        
        return helper(0, 0)

        