""" Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero. """

def threeSum(nums):
    ans = []
    for i in range(0,len(nums)-2):
        
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if (nums[i]+nums[j]+nums[k]) == 0:
                    ans.append([nums[i],nums[j],nums[k]])
    return ans


#Time complexity is O(n^3)

def threeSum(nums):
    hashSet = {}
    ans=set()
    #create a hash set to kepp the count of frequency of the elements
    for f in range(0,len(nums)):
        
        hashSet[nums[f]] = hashSet.get(nums[f], 0) + 1
    for i in range(0,len(nums-1)):
        hashSet[nums[i]] = hashSet[nums[i]] - 1
        for j in range(0,len(nums)):
             hashSet[nums[j]] = hashSet[nums[j]] - 1
             if -(nums[i]+nums[j]) in hashSet:
                 ans.add(sort([nums[i],nums[j], -(nums[i]+nums[j])]))
             hashSet[nums[j]] = hashSet[nums[j]] + 1
        hashSet[nums[i]] = hashSet[nums[i]] + 1
    return ans

    
def threeSum(nums):
    nums = sorted(nums)
    ans = []
    for i in range(0,len(nums)-2):
        if(i == 0 or (i>0 and nums[i]!=nums[i-1])):
            low = i+1
            high = len(nums) -1 
            while low < high:
                if nums[low] + nums[high] == -nums[i]:
                    ans.append([nums[low],nums[high],nums[i]])
                    while (low<high and nums[low] == nums[low+1]): 
                        low = low+1
                    while (low<high and nums[high]== nums[high-1]): 
                        high = high -1
                    low = low +1
                    high = high -1
                elif (nums[low]+nums[high]) < -nums[i]: low = low+1
                else: high = high - 1
    return ans

            


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))