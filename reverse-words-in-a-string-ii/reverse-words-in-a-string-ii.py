class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #reverse the string 
        s.reverse()
        temp1 , temp2 = 0 , 0
        end = len(s)
        
        while temp2 < end:
            while temp2 < end and s[temp2]!= ' ':
                temp2+=1
            temp3 = temp2-1
            while temp3 > temp1:
                s[temp3],s[temp1] = s[temp1],s[temp3]
                temp1+=1
                temp3-=1
            temp2+=1
            temp1 = temp2

                