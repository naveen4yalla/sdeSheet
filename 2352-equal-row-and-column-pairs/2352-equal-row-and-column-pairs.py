class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # initialize a dictionary to hold the count of unique rows
        counter={}
        # for each row in th grid, if it's present increae the count or set the count as 1
        for ele in grid:
            if str(ele) in counter:
                counter[str(ele)]+=1
            else: counter[str(ele)]=1
        # This is how it looks for test case 2
        # {'[3, 1, 2, 2]': 1, '[1, 4, 4, 5]': 1, '[2, 4, 2, 2]': 2}
        # transpose the grid for easy navigating
        grid_t=[[grid[j][i] for j in range(len(grid))]for i in range(len(grid[0]))]  
        matching=0
        # for each row in the transponsed grid(remember these are columns in the original grid)
        # if there is a match, increase the matching counter variable 
        for ele in grid_t:
            if str(ele) in counter:
                matching+=counter[str(ele)]      
        return matching