from collections import defaultdict
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topologicalSortDfs(self,visited,node,stack):
        visited[node] = 1
        for f in self.graph[node]:
            if visited[f] == -1:
                self.dfsUtil(visited,f,stack)
        stack.append(node)
        
                
                
    def dfs(self):
        visited = [-1] * len(self.graph)
        stack = []
        for f in range(0,len(self.graph)):
            if visited[f] == -1:
                self.topologicalSortDfs(visited,f,stack)
        return stack
                
                



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.dfs())