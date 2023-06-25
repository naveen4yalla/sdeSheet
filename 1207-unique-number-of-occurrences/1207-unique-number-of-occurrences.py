class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h1 = {}
        for f in arr:
            if f not in h1 :
                h1[f] = 1
            else:
                h1[f] += 1
        s1 = set(h1.values())
        return len(s1) == len(h1)
        