class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        k = len(maze)
        n = len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        stack = []
        seen = set()
        stack.append([start[0],start[1]])
        seen.add((start[0],start[1]))
        while stack:
            jk,lk = stack.pop()
            for f in directions:
                ab= jk
                bc = lk
               
                while 0 <= ab <k and 0 <= bc < n and maze[ab][bc] == 0:
                    ab = f[0]+ab
                    bc = f[1]+bc
                ab = ab - f[0]
                bc = bc  - f[1]

                if destination[0] == ab and  bc == destination[1]:
                    return True
                if (ab,bc) not in seen:
                    print(ab,bc)
                    seen.add((ab,bc))
                    stack.append([ab,bc])
        return False
        