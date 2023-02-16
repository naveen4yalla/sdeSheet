from collections import defaultdict
class Solution:
    def __init__(self):
        self.timer = 0
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def stronglyConnectedComponentsUtil(self,timeOfInsertion,lowInsertion,stackMember,i, st):
        timeOfInsertion[i] = self.timer
        lowInsertion[i] = self.timer
        self.timer+=1
        stackMember[i] = True
        st.append(i)
        for j in self.graph[i]:
            if timeOfInsertion[i] == -1:
                self.stronglyConnectedComponentsUtil(timeOfInsertion,timeOfInsertion,lowInsertion,stackMember,i, st)
                lowInsertion[i] = min(lowInsertion[i], lowInsertion[j])
            elif stackMember[j]== True:
                lowInsertion[i] = min(lowInsertion[i],lowInsertion[j])
    
        w = -1 # To store stack extracted vertices
        if lowInsertion[i] == timeOfInsertion[i]:
            while w != i:
                w = st.pop()
                print(w, end=" ")
                stackMember[w] = False

            print()
    def stronglyConnectedComponents(self):
        timeOfInsertion = [-1] * len(self.graph)
        lowInsertion = [-1] * len(self.graph)
        stackMember = [False] * len(self.graph)
        st = []
        for i in self.graph:
            if timeOfInsertion[i] != -1:
                self.stronglyConnectedComponents(timeOfInsertion,lowInsertion,stackMember,i, st )
        
g1 = Solution()
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("SSC in first graph ")
g1.stronglyConnectedComponents()