class Solution:
    def maxVowels(self, s, k):
        right = 0
        left = 0
        count = 0
        maxCount = 0
        v = {'a', 'e', 'i', 'o', 'u'}
        while right<len(s):
            if right < k:
                if s[right] in v:
                    count = count + 1
                    maxCount = count
            else:
                if s[right] in v:
                    count +=1
                if s[right-k] in v:
                    count-=1
                maxCount = max(count,maxCount)
            right+=1
        return maxCount
                    
                
            
        