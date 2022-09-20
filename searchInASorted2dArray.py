#The naive solution is to do a linear search 
# Binary Search
def search(matrix,target):
    j = len(matrix[0]) - 1
    i = 0
    while i<len(matrix) and  j>=0:
        if matrix[i][j] == target:
            return i,j
        if matrix[i][j]> target:
            j = j -1
        else:
            i = i+1
print(search([[1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]], 34))
        
    