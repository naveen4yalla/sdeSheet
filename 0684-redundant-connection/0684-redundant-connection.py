class UnionFind():
    def __init__(self,n):
        self.parent = [0] * (n + 1)
        for f in range(n+1):
            self.parent[f] = f
        self.rank = [0] * (n + 1)
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x1 , x2 = self.find(x) ,self.find(y)
        if x1==x2:
            return False
        elif self.rank[x1] < self.rank[x2]:
            self.parent[x1] = x2
        elif self.rank[x1] > self.rank[x2]:
            self.parent[x2] = x1
        else:
            self.parent[x2] = x1
            self.rank[x1]+=1
        return True
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(1000)
        for edge in edges:
            if not dsu.union(edge[0],edge[1]):
                return edge
        
        