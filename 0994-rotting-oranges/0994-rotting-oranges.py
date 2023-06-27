class Solution:
    def orangesRotting(self,grid):
        rows_length=len(grid)
        cols_length=len(grid[0])
        freshOranges=0
        minutesElapsed=-1
        queue=deque(())
        directions=[[-1,0],[0,1],[0,-1],[1,0]]

        #count the freshoranges
        for f in range(rows_length):
            for i in range(cols_length):
                if grid[f][i]==2:
                    queue.append((f,i))
                elif grid[f][i]==1:
                    freshOranges+=1
        # -1,-1 is end breakpoint for each minute elapsed
        queue.append((-1,-1))
        while queue:
            a,b=queue.popleft()
            if a==-1:
                minutesElapsed+=1
                if queue:
                    queue.append((-1,-1))
            else:
                for i,n in directions:
                    if rows_length > (i+a) >= 0 and cols_length > (n+b) >= 0:
                        if grid[i+a][n+b]==1:
                            grid[i+a][n+b]=2
                            freshOranges-=1
                            queue.append((i+a,n+b))
        if freshOranges==0:
            return minutesElapsed
        else:
            return -1
        