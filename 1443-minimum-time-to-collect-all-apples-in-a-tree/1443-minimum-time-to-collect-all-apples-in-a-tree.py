from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        ds = defaultdict(list)
        for i, j in edges:
            ds[i].append(j)
            ds[j].append(i)
        
        def dfs(root, par):
            if root is None:
                return 0
            
            time = 0
            for nei in ds[root]:
                if nei == par:
                    continue
                childTime = dfs(nei, root)
                if childTime or hasApple[nei]:
                    time += childTime + 2  # 2 seconds for walking to child and returning back
            return time
        
        return dfs(0, -1)

        