class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.rsearch(nums,target,0,len(nums)-1)
    def rsearch(self,nums,target,low,high):
        if high>=low:
            mid=(low+high)//2 # l + ((r - l) // 2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return self.rsearch(nums,target,low,mid-1)
            else:
                return self.rsearch(nums,target,mid+1,high)
        return -1
        