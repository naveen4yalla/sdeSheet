class Solution:
    def reverseString(self, s: List[str]) -> None:
        i , j = 0 , len(s) - 1
        while i < j:
            #inplace operation to change the places
            s[i],s[j] = s[j],s[i]
            #increment the indexes
            i+=1
            j-=1
        return s
        
        