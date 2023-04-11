class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the elements
        intervals.sort(key=lambda x:x[0])
        output = [] 
        for f in intervals:
            if not output or output[-1][1]<f[0]:
                output.append(f)
            else:
                output[-1][1] = max(f[1],output[-1][1])
        return output