class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.lstrip()
        s = s.rstrip()
        s = s.split()
        return len(s[-1])
        