class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        seen = set()
        for c in s:
            if c in seen:
                seen = set()
                res+=1
            seen.add(c)
        return res
        