# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         if len(word1) == 0: return word2
#         if len(word2) == 0: return word1
        
#         m = 0
#         n = 0
#         result = ""
#         while m != len(word1) and n != len(word2):
#             result = result + word1[m] + word2[n]
#             m+=1
#             n+=1
#         if m!= len(word1): return result+word1[m:]
#         if n!= len(word2): return result+word2[n:]
        
#         return result
        
#one pointer technique
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return "".join(result)
        
        