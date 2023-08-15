class UF:
    def __init__(self, n):
        self.n = n
        self.parent = [f for f in range(n+1)]
        self.rank = [1] * (n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    
    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1]+=self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2]+=self.rank[p1]
            self.parent[p1] = p2
        self.n -= 1
        return 1
    def isConnected(self):
        return self.n <= 1
    


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        alice = UF(n)
        bob = UF(n)
        for t , src , dst in edges:
            if t == 3:
                count += alice.union(src,dst) | bob.union(src,dst)
        for t ,src, dst in edges:
            if t == 1:
                count +=alice.union(src,dst)
            elif t == 2:
                count+= bob.union(src,dst)
        if bob.isConnected() and alice.isConnected():
            return len(edges) - count
        return -1
        
        # Your solution logic here
