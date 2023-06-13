# #Brute foce solution
# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         result = set()
#         for f in range(0,len(s)-2):
#             for i in range(f+1,len(s)-1):
#                 for j in range(i+1,len(s)):
#                     if (s[f]+s[i]+s[j]) == (s[j]+s[i]+s[f]):
#                         result.add(s[f]+s[i]+s[j])
#         return len(result)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        left = set()
        right = collections.Counter(s)
        for f in range(len(s)):
            right[s[f]]-=1
            if right[s[f]] == 0:
                right.pop(s[f])
            for j in range(26):
                c = chr(ord('a')+j)
                if c in left and c in right:
                    result.add((s[f],c))
            left.add(s[f])
        return len(result)