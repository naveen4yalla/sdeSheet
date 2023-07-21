class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        n = len(intervals)
        new_interval = [value, value]
        i = 0
        
        while i < n:
            interval = intervals[i]
            if new_interval[1] + 1 < interval[0]:
                break
            elif new_interval[0] - 1 > interval[1]:
                i += 1
                continue
            else:
                new_interval[0] = min(new_interval[0], interval[0])
                new_interval[1] = max(new_interval[1], interval[1])
                intervals.pop(i)
                n -= 1
        
        self.intervals.insert(i, new_interval)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()