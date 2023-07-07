# class Solution(object):
#     def maxUncrossedLines(self, nums1, nums2):
#         n1 = len(nums1)
#         n2 = len(nums2)

#         memo = {}

#         def solve(i, j):
#             if i <= 0 or j <= 0:
#                 return 0

#             if (i, j) in memo:
#                 return memo[(i, j)]

#             if nums1[i - 1] == nums2[j - 1]:
#                 memo[(i, j)] = 1 + solve(i - 1, j - 1)
#             else:
#                 memo[(i, j)] = max(solve(i - 1, j), solve(i, j - 1))
#             return memo[(i, j)]

#         return solve(n1, n2)
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [0] * (n2 + 1)
        dpPrev = [0] * (n2 + 1)

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = 1 + dpPrev[j - 1]
                else:
                    dp[j] = max(dp[j - 1], dpPrev[j])
            dpPrev = dp[:]

        return dp[n2]