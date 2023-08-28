class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxi = 0
        for char in s:
            if char == '(':
                stack.append(char)
                if len(stack) > maxi:
                    maxi = len(stack)
            elif char == ')':
                stack.pop(-1)
        return maxi