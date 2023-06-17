class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        #two pointer approach 
        for j in range(len(nums)):
            if nums[i]!=nums[j]:
                i+=1;
                nums[i]=nums[j]
        return i+1
        