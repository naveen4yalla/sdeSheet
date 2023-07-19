class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        
        def backtrack(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i >= len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            count = 0
            if s[i] == t[j]:
                count += backtrack(i + 1, j + 1)
            
            count += backtrack(i + 1, j)
            
            cache[(i, j)] = count
            
            return count
        
        return backtrack(0, 0)
