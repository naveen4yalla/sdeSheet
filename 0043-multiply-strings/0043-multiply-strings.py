class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #check if there are any 0 in any string 
        if "0" in [num1 ,num2]:
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1)+len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                result[i+j] = result[i+j] + digit
                result[i+j+1] = result[i+j+1] + (result[i+j]//10)
                result[i+j] = result[i+j]%10
        result = result[::-1]
        beg = 0
        while beg < len(result) and result[beg]==0:
            beg = beg + 1
        result = map(str,result[beg:])
        return "".join(result)
        
                
                
        
        