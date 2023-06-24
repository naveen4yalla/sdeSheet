class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1),len(word2)
        i,j = 0,0
        res = ''
        while i<m and j<n:
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
            
        if i<m:
            res += word1[i:]
        if j<n:
            res += word2[j:]
        return res
        
#one pointer technique
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         result = []
#         n = max(len(word1), len(word2))
#         for i in range(n):
#             if i < len(word1):
#                 result += word1[i]
#             if i < len(word2):
#                 result += word2[i]

#         return "".join(result)
        
        