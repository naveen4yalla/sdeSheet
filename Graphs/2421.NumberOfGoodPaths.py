from collections import defaultdict
class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self,i):
        while i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
            i = self.parent[i]
        return i
    def union(self,a,b):
        aroot = self.find(a)
        broot = self.find(b)

        if aroot == broot:
            return False
        if self.rank[aroot] > self.rank[broot]:
            self.parent[broot] = aroot
        elif self.rank[broot] > self.rank[aroot]:
            self.parent[aroot] = broot
        else:
            self.rank[aroot]+=1
            self.parent[broot] = aroot
        return True 

        
class Solution:
    def numberOfGoodPaths(self, vals, edges):
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        valToIndex = defaultdict(list)
        for i , val in enumerate(vals):
            valToIndex[val].append(i)
        
        res = 0
        uf= UnionFind(len(vals))
        for val in sorted(valToIndex.keys()):
            for i in valToIndex[val]:
                for n in graph[i]:
                    if vals[i]>= vals[n]:
                        uf.union(n,i)
            count = defaultdict(int)
            for i in valToIndex[val]:
                count[uf.find(i)] += 1
                res += count[uf.find(i)]
        return res