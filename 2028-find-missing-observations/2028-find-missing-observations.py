class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        count = len(rolls) + n
        mTotal = sum(rolls)
        nTotal = (mean * count) - mTotal
        
        if nTotal > 6 * n or nTotal < n:
            return []
        res = []
        while nTotal:
            dice = min(nTotal - n + 1, 6)
            res.append(dice)
            nTotal -= dice
            n -= 1
        return res
        
            
        