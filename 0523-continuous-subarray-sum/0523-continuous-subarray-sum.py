class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder_hashmap = {}
        reminder_hashmap[0] = -1
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum%k in reminder_hashmap.keys():
                if i-reminder_hashmap[sum%k]>=2:
                    return True
                else:
                    continue
            reminder_hashmap[sum%k] = i
        return False
            

            
            
            
            
            
