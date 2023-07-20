class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        prev = intervals[0][1]
        for start , end in intervals[1:]:
            if start >= prev:
                prev = end
            else:
                count+=1
                prev = min(end,prev)
        return count

                
                
                
