class Solution:
    def countComponents(self, n, edges) -> int:
        s = UnionFind(n)
        for a,b in edges:
            s.union(a,b)
        
        parent = set()
        for i in range(n):
            parent.add(s.find(i))
        return len(parent)
                
class UnionFind:
    def __init__(self,size):
        self.root=[f for f in range(size)]
        self.rank=[1]*size
    def find(self,n):
        if self.root[n]==n:
            return n
        self.root[n]=self.find(self.root[n])
        return self.root[n]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx==rooty:
            return 
        if rootx!=rooty:
            if  self.rank[rootx]>self.rank[rooty]:
                self.root[rooty]=rootx
            elif self.rank[rootx]<self.rank[rooty]:
                 self.root[rootx]=rooty
            else:
                 self.root[rooty]=rootx
                 self.rank[rootx]=self.rank[rootx]+1