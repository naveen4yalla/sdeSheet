class Solution:

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left, right = 0, len(removable)
    
        while left <= right:
            mid = (left + right) // 2
            modified_s = list(s)

            # Mark the first `mid` characters as removed
            for i in range(mid):
                modified_s[removable[i]] = '#'

            # Check if `p` is still a subsequence of `modified_s`
            if isSubsequence(modified_s, p):
                left = mid + 1
            else:
                right = mid - 1

        return right
 
def isSubsequence(s, p):
    i, j = 0, 0
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            j += 1
        i += 1
    return j == len(p)
