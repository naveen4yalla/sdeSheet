class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            if stack[-1][1] == k:
                stack.pop()
        
        result = ""
        for c , count in stack:
            result = result + c*count
        return result
            
        