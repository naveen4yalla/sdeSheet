class Solution:
    def canPermutePalindrome(self, s):
        lt = {}
        for f in s:
            if f not in lt:
                lt[f] = 1
            else:
                lt[f]=lt[f]+1
            if lt[f] == 2:
                del lt[f]
        return len(lt) <=1
        
        