class Solution:
    def isValid(self,s):
        mapping = {"(": ")", "[": "]",  "{": "}"}
        open_parameters = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_parameters:
                stack.append(i)
            elif stack and i == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
                
