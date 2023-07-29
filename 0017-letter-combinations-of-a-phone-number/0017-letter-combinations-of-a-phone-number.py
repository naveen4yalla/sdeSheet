class Solution:
    def letterCombinations(self,digits):
        result = []
        n = len(digits)
        if n==0:
            return []
        keypad = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backTrack(index,temp):
            if n == index:
                result.append(temp)
                return 
            for i in keypad[digits[index]]:
                backTrack(index+1,temp+i)
                
        backTrack(0,"")
        return result