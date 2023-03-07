class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=set()
        maxlen=0
        left=0
        right=0
        
        while right < len(s):
            if s[right] not in x:
                x.add(s[right])
                right += 1
                maxlen = max(maxlen,len(x))
            else:
                x.remove(s[left])
                left += 1
        return maxlen
                
