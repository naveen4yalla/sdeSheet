from collections import defaultdict

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        indegree = [0] * n
        tempGraph = defaultdict(list)
        
        for i, neighbors in enumerate(graph):
            for j in neighbors:
                tempGraph[j].append(i)
                indegree[i] += 1
        
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        safeNode = [False] * n
        while queue:
            popElement = queue.pop(0)
            safeNode[popElement] = True
            for n in tempGraph[popElement]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        
        result = []
        for i in range(len(graph)):
            if safeNode[i]:
                result.append(i)
        return result