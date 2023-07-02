class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ls = defaultdict(list)
        for  i,j in roads:
            ls[i].append(j)
            ls[j].append(i)
        visited = set()
        result = [0]
        def dfs(n,parent):
            passengers = 0
            for i in ls[n]:
                if i!=parent:
                    p = dfs(i,n)
                    passengers+=p
                    result[0] += int(ceil(p/seats))
            return passengers+1
        dfs(0,-1)
        return result[0]