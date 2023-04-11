class Solution:
    def findLengthOfLCIS(self, nums: List[int]):
        result = 1
        maxresult = 1
        for f in range(1,len(nums)):
            if nums[f-1]<nums[f]:
                result = result + 1
                maxresult = max(result,maxresult)
            else:
                result = 1
        return maxresult