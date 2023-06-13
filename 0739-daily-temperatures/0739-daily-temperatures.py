class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #use a monotonic stack to push the indexes 
        n=len(T)
        days_of_wait=[0]*n
        s=[]
        for i in range(n):
            while(len(s) != 0 and   T[s[-1]] < T[i]):
                days_of_wait[s[-1]] = i - s[-1]
                s.pop(-1)
            s.append(i)

        return days_of_wait