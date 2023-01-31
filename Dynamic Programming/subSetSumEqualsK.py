a = [2,3,1,1]
class Solution:
    def subSetSumEqualsK(self,index,target):
        if target == 0:
            return True
        if index == 0:
            return a[0] == target
       
        notTake = self.subSetSumEqualsK(index-1,target)
        take= False
        if target>=a[index]:
            take = self.subSetSumEqualsK(index-1,target - a[index])
        return notTake or take
s = Solution()
print(s.subSetSumEqualsK(len(a)-1,4))
            
        
        
    