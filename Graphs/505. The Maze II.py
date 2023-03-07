class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        k = len(maze)
        n = len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = []
       # seen = set()
        queue.append([start[0],start[1]])
        #seen.add((start[0],start[1]))
        distance=[[10000 for i in range(n)] for j in range(k)]
        distance[start[0]][start[1]] = 0
        while queue:
            jk,lk = queue.pop(0)
            for f in directions:
                ab= jk
                bc = lk
                ab = f[0]+ab
                bc = f[1]+bc
                count = 0
                while 0 <= ab <k and 0 <= bc < n and maze[ab][bc] == 0:
                    ab = f[0]+ab
                    bc = f[1]+bc
                    count = count + 1
                #ab = ab - f[0]
                #bc = bc  - f[1]

                #if destination[0] == ab and  bc == destination[1]:
                    #return True
                # if (ab,bc) not in seen:
                #     seen.add((ab-f[0],bc-f[1]))
                #     stack.append([ab-f[0],bc-f[1]])
                if distance[jk][lk]+count < distance[ab-f[0]][bc-f[1]]:
                    distance[ab-f[0]][bc-f[1]] = distance[jk][lk]+count
                    queue.append([ab-f[0],bc-f[1]])
                    
        if distance[destination[0]][destination[1]] == 10000:
            return -1
        else:
            return distance[destination[0]][destination[1]]