class Solution:
    def countingsort(self,test):
       count = [0]*len(test)
       for f in test:
           count[f] = count[f] + 1
       temp = []
       for i in range(0,len(count)):
           if count[i]>1:
               temp.append(i)
       return temp
           
    def missingNumbers(self,test):
        self.countingsort(test)


test = [3,1,2,5,4,6,7,5]
s = Solution()
s.missingNumbers(test)