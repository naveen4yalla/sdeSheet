def nextGreaterElement(nums):
    stack= [ ]
    nge=[-1]*len(nums)
    s = len(nums)
    for i in range(s*2-1,-1,-1):
        while(stack and stack[-1]<=nums[i%s]):
            stack.pop()
        if i<s:
            if stack:
                nge[i] = stack[-1]
            
            
        stack.append(nums[i%s])
    print(nge) 
nextGreaterElement([5,7,1,2,6,0])