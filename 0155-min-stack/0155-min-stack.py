class MinStack:

    def __init__(self):
        self.stack,self.min_stack=[],[]
        self.size=0

    def push(self, val: int) -> None:
        if self.size==0:
            self.min_stack.append(val)
        else:
            if val<=self.min_stack[-1]:
                self.min_stack.append(val)
        self.stack.append(val)
        self.size=self.size+1

    def pop(self) -> None:
        temp=self.stack.pop()
        if temp==self.min_stack[-1]:
            self.min_stack.pop()
        self.size=self.size-1

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()