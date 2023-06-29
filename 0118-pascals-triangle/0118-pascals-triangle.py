class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        result =[[1],[1,1]]
        for f in range(2,numRows):
            temp=[1,1]
            for i in range(1,f):
                temp.insert(i,result[f-1][i-1]+result[f-1][i])
            result.append(temp)
        return result
        