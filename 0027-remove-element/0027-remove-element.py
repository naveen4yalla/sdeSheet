class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left ,right = 0 , 0 
        for i in range(len(nums)):
            if nums[right]!= val:
                nums[left],nums[right] = nums[right] ,nums[left]
                left +=1
            right+=1
        return left