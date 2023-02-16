from collections import defaultdict,deque,Counter
class Solution:
    def findOrder(self,alienList):
        newAlienlist = defaultdict(list)
        in_degree = Counter({char: 0 for word in alienList for char in word})
        for i in range(0,len(alienList)-1):
            n = min(len(alienList[i]),len(alienList[i+1]))
            temp1 , temp2 = alienList[i] , alienList[i+1]
            for j in range(0,n):
                if temp1[j]!=temp2[j]:
                    newAlienlist[temp1[j]].append(temp2[j])
                    in_degree[temp2[j]] += 1
                    break
        #Topological sort
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        sortElement =  []
        while queue:
            n = queue.popleft()
            sortElement.append(n)
            print(newAlienlist[n])
            for f in newAlienlist[n]:
                if in_degree[f]!=0:
                   in_degree[f] = in_degree[f] - 1
                if in_degree[f]==0:
                    queue.append(f)
                    
        if len(sortElement) == len(in_degree):
            return ''.join(sortElement)
        else:
            return ""