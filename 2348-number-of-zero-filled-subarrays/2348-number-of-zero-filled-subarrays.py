class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0 
        subarray = 0
        for i in nums:
            if i == 0:
                subarray+=1
            else:
                subarray = 0
            ans+=subarray
        return ans
                
        