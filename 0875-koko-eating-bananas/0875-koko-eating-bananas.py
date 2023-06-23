class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left  = 1
        right = max(piles)
        result = right
        while left<=right:
            mid = (left + right)//2
            hours = 0
            for i in piles:
                hours =  hours + math.ceil(i/mid)
            if hours <=h:
                result = min(result,mid)
                right = mid - 1
            else:
                left = mid +1
        return result
                
                
                