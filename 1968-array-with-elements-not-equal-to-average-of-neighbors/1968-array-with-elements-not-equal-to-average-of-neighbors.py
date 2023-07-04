class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        l=0
        r=len(nums) -1
        while len(nums)!=len(result):
            result.append(nums[l])
            l+=1
            if l<r:
                result.append(nums[r])
                r-=1
        return result
            
        