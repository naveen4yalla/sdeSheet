from tempfile import tempdir


# Input: N=6, 
# arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00} 
# dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}

# Output:3
# Time complexity is O(n^2)
#SpaceComplexity is O(n^2)
import heapq
def minimumNumberOfPlatforms(n,arr,dep):
    arrivalDeparture = [ ]
    for f in range(n):
        arrivalDeparture.append([arr[f],dep[f]])
    arrivalDeparture.sort(key=lambda x:x[0])
    occupied = [arrivalDeparture[0][1]]
    heapq.heapify(occupied)
    max = 0
    temp =1
    for f in range(n):
        if f == 0:
            return 
        if temp!=0:
            for i in occupied:
                if i<arrivalDeparture[f][0]:
                    temp = temp -1
                    temp = temp + 1
                    heapq.heappop(occupied)
                else:
                    temp = temp+1
                max = max(temp,max)
        else:
            temp = temp + 1
        heapq.heappush(arrivalDeparture[f][1])
            
               
            
            
            
        
        
        
        