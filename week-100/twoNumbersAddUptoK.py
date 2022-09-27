#Two Numbers added 
#[21,60]=81
#Using two sum tweaked gives the result 
def find_sum(lst, k):
    dict = {}
    for f in range(len(lst)):
        if k - lst[f] in dict :
            return [k-lst[f],lst[f]]
        else:
            dict[lst[f]] = f
find_sum([1,21,3,14,5,60,7,6],81)


#Method 1:
#Brute Force

#Sort the array