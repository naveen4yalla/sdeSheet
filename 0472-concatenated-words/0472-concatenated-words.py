#Brute force 
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        wordSet = set(words)
        dp = {}
        def dfs(word):
            if word in dp:
                return dp[word]
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if((prefix in wordSet and suffix in wordSet) or (prefix in wordSet and dfs(suffix))):
                    dp[word] = True
                    return True
            dp[word] = False
            return dp[word]
        res =[]
        for w in words:
            if dfs(w):
                res.append(w)
        return res
        
        
        