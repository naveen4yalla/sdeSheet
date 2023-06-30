class Solution:
    def isBipartite(self, graph):
        def dfs(f,colour):
            colours[f] = colour
    
            for j in graph[f]:
                if colours[j] == -1:
                    
                    if(dfs(j,colour^1)) == False:
                        return False
                elif colours[j] == colour:
                    return False
            return True

        
        colours = [-1] * len(graph)
        for f in range(len(graph)):
            if colours[f] == -1:
                if dfs(f,0) == False:
                    return False
        return True