class Solution:
    def subsets(self,nums):
        result = []
        subset = []
        def backTrack(index):
            if len(nums) == index:
                result.append(subset.copy())
                return 
            subset.append(nums[index])
            backTrack(index+1)
            subset.pop()
            backTrack(index+1)
        backTrack(0)
        return result
s = Solution()
print(s.subsets([1,2,3]))