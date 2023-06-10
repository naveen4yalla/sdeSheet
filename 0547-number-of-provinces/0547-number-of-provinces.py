class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            seen[i] = True
            for f in range(len(seen)):
                if isConnected[i][f]!= 0 and seen[f] == False:
                    dfs(f)

        seen = [False for _ in range(len(isConnected))]
        count = 0
        for i in range(len(seen)):
            if seen[i] == False:
                count+=1
                dfs(i)
        return count