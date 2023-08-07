class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = 0
        s =set()
        for right in range(len(nums)):
            if right - left > k:
                s.remove(nums[left])
                left+=1
            if nums[right] in s:
                return True
            s.add(nums[right])
        return False
        
        
        