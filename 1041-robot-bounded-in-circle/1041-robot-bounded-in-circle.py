class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0 , 0 
        dirx ,diry = 0 , 1
        for f in instructions:
            if f == "G":
                x ,y = x + dirx , y + diry
            elif f == "L":
                dirx , diry = diry *-1 , dirx
            else:
                dirx , diry = diry , dirx *-1 
        return (x,y) == (0,0) or (dirx,diry) != (0,1)