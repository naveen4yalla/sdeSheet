class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)
        for i,j in enumerate(edges):
            graph[i].append(j)
            
        def bfs(node,sh1map):
            queue = []
            queue.append([node,0])
            sh1map[node] = 0
            while queue:
                a , b = queue.pop(0)
                for i  in graph[a]:
                    if i not in sh1map:
                        queue.append([i, 1 + b])
                        sh1map[i] =  1 +b 
            
        sh1_map = {}
        sh2_map = {}
        bfs(node1,sh1_map)
        bfs(node2,sh2_map)
        distance = float("inf")
        n = -1
        for i in range(len(edges)):
            if i in sh1_map and i in sh2_map:
                temp = max(sh1_map[i],sh2_map[i])
                if temp < distance:
                    n = i
                    distance = temp
        return n
        