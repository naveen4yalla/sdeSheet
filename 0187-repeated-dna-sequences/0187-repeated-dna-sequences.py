class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 10
        seen = set()
        output = set()
        for i in range(len(s)-left + 1):
            t = s[i:i+left]
            if t in seen:
                output.add(t[:])
            seen.add(t)
        return output
        