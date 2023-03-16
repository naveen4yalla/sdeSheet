class Solution:
    def generateParenthesis(self,n):
        result = []
        open = 1
        close = 0
        def backTrack(open,close,temp):
            #append into result when the opena and count == n
            if open == n and close == n:
                result.append(temp)
                return
            if close < open:
                
                backTrack(open,close+1,temp+")")
            if open<n:
                
                backTrack(open+1,close,temp+"(")
        backTrack(open,close,"(")
        return result
s = Solution()
print(s.generateParenthesis(3))