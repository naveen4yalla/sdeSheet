def removeDuplicates(nums):
    i = 0
    for f in range(0,len(nums)):
        if nums[i]!=nums[f]:
            i = i+1
            nums[i] = nums[j]
    return i 
    
