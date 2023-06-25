class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        prefix = 0
        for i in range(0,len(gain)):
            result = max(prefix+gain[i],result)
            prefix = prefix+gain[i]
        return result
            
        