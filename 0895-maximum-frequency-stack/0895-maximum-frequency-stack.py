class FreqStack:

    def __init__(self):
        self.countOfVal = {}
        self.maxCount = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.countOfVal[val] = self.countOfVal.get(val, 0) + 1
        valCount = self.countOfVal[val]
        
        if self.maxCount < valCount:
            self.maxCount = valCount
            self.stacks[valCount] = []
        
        self.stacks[valCount].append(val)
        

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.countOfVal[res] -= 1
        if len(self.stacks[self.maxCount]) == 0:
            del self.stacks[self.maxCount]
            self.maxCount -= 1
        
        return res
