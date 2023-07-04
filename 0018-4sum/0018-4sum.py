class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        quad = []
        def kSum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i > start and nums[i-1] == nums[i]:
                        continue
                    else:
                        quad.append(nums[i])
                        kSum(k-1,i+1,target - nums[i])
                        quad.pop()
                return
            else:
                left = start 
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] < target:
                        left+=1
                    elif nums[right] + nums[left] > target:
                        right-=1
                    else:
                        result.append(quad+[nums[left],nums[right]])
                        left+=1
                        while left < right and nums[left-1] == nums[left]:
                            left+=1
        nums.sort()
        kSum(4,0,target)
        return result
                        
        