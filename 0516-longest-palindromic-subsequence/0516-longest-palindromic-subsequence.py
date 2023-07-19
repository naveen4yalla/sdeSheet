class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def helper(left,right):
            if left > right:
                return 0
            if left == right:
                return 1
            if s[left] == s[right]:
                return 2 + helper(left + 1 ,right -1)
            else:
                return max(helper(left +1 ,right) , helper(left,right - 1)) 
        return helper(0,len(s)-1)

            
        