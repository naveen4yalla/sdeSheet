class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        count = 0
        while len(ans) > count:
            if len(nums)<=count:
                ans[count]=nums[(count%len(nums))]
            else:
                ans[count] = nums[count]
            count+=1
        return ans
        