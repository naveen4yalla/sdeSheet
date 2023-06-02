class Solution:
    def reverseWords(self, s: str) -> str:
        #split the string into array
        s  = s.split()
        for f in range(0,len(s)):
            #pop and insert the element
            s.insert(f,s.pop())
        #return the array as string
        return " ".join(s)