class Solution:
    def removeStars(self, s: str) -> str:
        
        st = []
        for f in range(0,len(s)):
            if s[f] == "*":
                st.pop()
            else:
                st.append(s[f])
        return "".join(st)
            
                
        