class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for f in range(len(s)-k + 1):
            if s[f:k] not in seen:
                seen.add(s[f:f+k])
        return len(seen) == 2 ** k
        