from collections import deque,defaultdict
class Solution:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices # No. of vertices'
        
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    
    def bfs(self,grid,visited,f):
        queue=deque(())
        queue.append((f,-1))
        visited[f] = True
        while queue:
            poppedElement = queue.popleft()
            for i in grid[poppedElement[0]]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append((i,poppedElement[0]))
                elif poppedElement[1]!=i:
                    return True
        return False
        
    
    
    
    
    
    
    
    def bfsCycle(self,grid):
        n = len(grid)
        visited = [False] * n
        for f in range(n):
            if visited[f] == False:
                if self.bfs(grid,visited,f):
                    print("Cycle Exist")
                
        
                
g =Solution(6)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(3,4)
g.addEdge(4,5)
g.bfsCycle(g.graph)