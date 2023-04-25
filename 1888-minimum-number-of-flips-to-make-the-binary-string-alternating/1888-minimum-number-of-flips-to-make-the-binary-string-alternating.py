class Solution:
    def minFlips(self, s: str) -> int:
        n= len(s)
        #increase the size of a string 
        s = s+s
        #atmost two possible differences can be created with the alternating binary numbers 
        #creating two possible string answers
        alt1 , alt2 = "",""

        for f in range(len(s)):
            alt1 += "1" if f%2==0 else "0"
            alt2 += "0" if f%2==0 else "1"
        left, right =0 , 0
        diff1 ,diff2 = 0 , 0 
        output = len(s)
        #Loop throught the string
        while right < len(s):
            if alt1[right] != s[right]:
                diff1 = diff1 + 1
            if alt2[right] != s[right]:
                diff2 = diff2 + 1
            
        #after crossing the initial window size reduces  the differences in the left index  and increase the left index 
            if right-left + 1 > n:
                if alt1[left] != s[left]:
                    diff1 = diff1 - 1
                if alt2[left] != s[left]:
                    diff2 = diff2 - 1
                left+=1
            if right-left + 1 == n:
                output = min(output,diff1,diff2)
            right = right + 1
        return output 


