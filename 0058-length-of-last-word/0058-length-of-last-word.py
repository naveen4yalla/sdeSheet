# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s= s.lstrip()
#         s = s.rstrip()
#         s = s.split()
#         return len(s[-1])
#alternative solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p , length = len(s) , 0
        while p>0:
            p-=1
            if s[p]!= ' ':
                length = length + 1
            elif length > 0:
                return length
        return length
                