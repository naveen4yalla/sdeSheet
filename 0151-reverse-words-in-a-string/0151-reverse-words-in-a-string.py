class Solution:
    def reverseWords(self, s: str) -> str:
        #split the string into array
        s  = s.split()
        for f in range(0,len(s)):
            #pop and insert the element
            s.insert(f,s.pop())
        #return the array as string
        return " ".join(s)

    
#implementation of deque approach 
# from collections import deque
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         left, right = 0, len(s) - 1
#         # remove leading spaces
#         while left <= right and s[left] == ' ':
#             left += 1
        
#         # remove trailing spaces
#         while left <= right and s[right] == ' ':
#             right -= 1
            
#         d, word = deque(), []
#         # push word by word in front of deque
#         while left <= right:
#             if s[left] == ' ' and word:
#                 d.appendleft(''.join(word))
#                 word = []
#             elif s[left] != ' ':
#                 word.append(s[left])
#             left += 1
#         d.appendleft(''.join(word))
        
#         return ' '.join(d)