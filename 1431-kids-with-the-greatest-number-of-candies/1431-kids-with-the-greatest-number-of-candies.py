class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximumCandy = max(candies)
        result = []
        for f in candies:
            if f+extraCandies >= maximumCandy:
                result.append(True)
            else:
                result.append(False)
        return result