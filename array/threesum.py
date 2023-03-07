class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #To store the result
        result = []
        #sort the elements in ana array
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and nums[i-1] == a:
                continue
            #initialise two pointerts 
            left , right = i+1 , len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right-=1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([a,nums[left],nums[right]])
                    left = left+1
                    #increase the left pointer to remove duplicates
                    while nums[left] == nums[left-1] and left < right:
                        left = left + 1
        return result