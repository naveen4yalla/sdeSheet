class Solution:
    def updateMatrix(self,List):
        queue=[]
        rows=len(List)
        cols=len(List[0])
        for f in range(0,rows):
            for i in range(0,cols):
                if List[f][i] == 0:
                    queue.append((f,i))
                else:
                    List[f][i]=float("inf")
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            x,y=queue.pop(0)
            for d1,d2 in directions:
                x1,y1=x+d1,y+d2
                if 0 <= x1 <rows and 0 <= y1 <cols and List[x1][y1]>List[x][y]:
                    queue.append((x1,y1))
                    List[x1][y1]=List[x][y]+1
        return List
            
                    
                    