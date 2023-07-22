#Brute force would be sorting the array and traversing the array 
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <=high:
            mid = low + ((high - low) // 2)
            if ((mid - 1 < 0 or nums[mid-1] != nums[mid]) and (mid +1 == len(nums) or nums[mid+1] != nums[mid])):
                return nums[mid]
             
            #decide which part should be put in range
            size =mid - 1 if nums[mid-1]== nums[mid] else mid
            
            if size % 2:
                high = mid -1
            else:
                low = mid + 1