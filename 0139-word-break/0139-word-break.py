class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            ans = False
            for word in wordDict:
                if word == s[i:i + len(word)]:
                    ans = dfs(i + len(word))
                    if ans:
                        break

            memo[i] = ans
            return ans

        return dfs(0)
                    
        