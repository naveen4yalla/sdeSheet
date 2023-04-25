class Solution:
    def minSwaps(self, s):
        #create a stack 
        #Dont need to consider about the balnced parenthesis in the string
        #reduce coutn if balanced parthensis is found 
        count = 0
        for f in s :
            if f == "[":
                count = count + 1
            elif count!=0:
                count = count -1
        return (count+1)//2
        
            
        