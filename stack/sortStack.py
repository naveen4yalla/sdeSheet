def sortStack(arr):
    stack = arr
    tempStack = []
    while stack:
        top = stack.pop()
        while tempStack and tempStack[-1]>top:
            stack.append(tempStack.pop())        
        
        
        tempStack.append(top)
            
        

sortStack([34,3,31,98,92,23])