from collections import defaultdict
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def dfsUtil(self,visited,path,node):
        visited[node] = 1
        path[node] = 1
        for f in self.graph[node]:
            if visited[f] == -1:
                if self.dfsUtil(visited,path,f) == True:
                    return True
            elif path[f] == 1:
                return True
        path[node] = -1
        return False
                
                
    def dfsCycle(self):
        visited = [-1] * len(self.graph)
        path = [-1] * len(self.graph)
        for f in range(0,len(self.graph)):
            if visited[f] == -1:
                if self.dfsUtil(visited,path,f) == True:
                    return True 
        return False
                
                



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.dfsCycle())