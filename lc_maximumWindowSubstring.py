#from collections import Counter
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s :
            return ""
        uniqueCharacters = Counter(t)
        required  = len(uniqueCharacters)
        formed = 0 
        left,right = 0, 0 
        window_counts = {}
        ans = float("inf"), None, None
        while right<len(s):
            window_counts[s[right]] = window_counts.get(s[right],0)  + 1
            if s[right]  in uniqueCharacters and window_counts[s[right]] == uniqueCharacters[s[right]]:
                formed = formed + 1
            while formed == required and left<=right:
                if right - left  < ans[0]:
                    ans = (right - left, left, right)
                window_counts[s[left]]  =  window_counts[s[left]] - 1
                if s[left] in uniqueCharacters and   window_counts[s[left]]< uniqueCharacters[s[left]]:
                    formed = formed -1
                left = left + 1
                
            right = right + 1 
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
