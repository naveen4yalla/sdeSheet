class Solution:
    def subsets(self,nums,sum):
        result = []
        subset = []
        def backTrack(index,num):
            if num==0:
                result.append(subset.copy())
            if index==len(nums):
                return     
            subset.append(nums[index])
            backTrack(index+1,num-nums[index])
            subset.pop()
            backTrack(index+1,num)
        backTrack(0,sum)
        return result
s = Solution()
print(s.subsets([1,2,3],3))