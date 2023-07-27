# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         memo = {}

#         def dfs(i):
#             if i == len(s):
#                 return True

#             if i in memo:
#                 return memo[i]

#             ans = False
#             for word in wordDict:
#                 if word == s[i:i + len(word)]:
#                     ans = dfs(i + len(word))
#                     if ans:
#                         break

#             memo[i] = ans
#             return ans

#         return dfs(0)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
















                    
        