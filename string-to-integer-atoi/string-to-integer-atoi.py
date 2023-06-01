class Solution:
    def myAtoi(self, str: str) -> int:
        #Declaring the max int value
        maxint = 2 ** 31 - 1
        #Declaring the min int value
        minint = -2 ** 31
        #Start of the index 
        i=0
        #neg is used to switch between plus and minus
        neg=1
        #to validate whether the string is consisting of given numbers 
        x = set('1234567890')
        #result is zero initially
        res=0
        #remove the whitespaces at the beginning 
        while i < len(str) and str[i] == ' ':
            i += 1
        if i < len(str) and str[i] == '-':
            neg = -1
            i += 1
        elif i < len(str) and str[i] == '+':
            i += 1
        #calculate  the sum 
        while i < len(str) and str[i] in x:
            res = res*10 + int(str[i])
            i += 1
        #add the plus or minus     
        res = res * neg
        #the value should be range between minimum and maximum 
        if neg == 1 and res > maxint:return maxint
        if neg == -1 and res < minint:return minint
        #return the reuslt
        return res

                
            
        