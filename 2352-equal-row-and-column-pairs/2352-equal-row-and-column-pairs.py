class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        counter={}
     
        for ele in grid:
            if str(ele) in counter:
                counter[str(ele)]+=1
            else: counter[str(ele)]=1
        grid_t=[[grid[j][i] for j in range(len(grid))]for i in range(len(grid[0]))]  
        matching=0
        for ele in grid_t:
            if str(ele) in counter:
                matching+=counter[str(ele)]      
        return matching