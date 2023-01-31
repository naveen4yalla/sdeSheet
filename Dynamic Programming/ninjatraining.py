
from functools import lru_cache
#Tabulation
def ninjaTrainingTabulation(n, points):

    dp = [[0 for i in range(4)] for j in range(n)]
    dp[0][0] = max(points[0][2],points[0][1])
    dp[0][1] = max(points[0][0],points[0][2])
    dp[0][2] = max(points[0][1],points[0][0])
    dp[0][3] = max(points[0][1],points[0][0])
    dp[0][3] = max( dp[0][3],points[0][2])
    
    for day in range(1,n):
        for last in range(0,4):
            dp[day][last] = 0
            for task in range(0,3):
                if task!= last:
                    point = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last],point)
    return dp[n-1][3]

#Memoization:
def ninjaMmeoizationMain(days,last,points):
    @lru_cache(maxsize=None)
    def ninjaMemoization(n,last):
        if n==0:
            maximum = 0
            for i in range(0,3):
                if last!=i:
                    maximum = max(maximum,points[0][i])
            return maximum 
        maximum = 0
        for i in range(0,3):
            if last!=i:
                point = max(points[n][i],ninjaMemoization(n-1,i))
                maximum = maximum(point,maximum)
        return maximum
    return ninjaMemoization(days,last)
print(ninjaMmeoizationMain(3,3,[[1 ,2 ,5],[3 ,1, 1],[3,3, 3]]))          
        

            