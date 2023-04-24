class Solution:
    def findMin(self, nums: List[int]) -> int:
        length=len(nums)
        if length==1:
            return nums[0]
        left,right=0,length-1
        #to check of no rotation
        if nums[right]>nums[0]:
            return nums[0]
        while right>=left:
            mid=left+(right-left)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid]>nums[0]:
                left=mid+1
            else:
                right=mid-1
        