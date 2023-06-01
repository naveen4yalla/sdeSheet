class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            #To remove white spaces from left 
            while i < j and not s[i].isalnum():
                i = i+1
            #To remove whitespaces from right
            while i < j and not s[j].isalnum():
                j = j -1
            #compare the values
            if s[i].lower() != s[j].lower():
                return False
            #increment the left 
            i = i+1
            #increment the right 
            j = j-1
        return True