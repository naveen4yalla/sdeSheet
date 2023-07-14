class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.arr[-1], self.dict[val]
            self.arr[idx], self.dict[last_element] = last_element, idx
            self.arr.pop()
            del self.dict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()