class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        def findCapacity(mid):
            weightPerDay = mid
            ships = 1
            for  i in weights:
                if weightPerDay - i < 0:
                    ships+=1
                    weightPerDay = mid
                weightPerDay-=i
            return ships<=days
                    
                
                
        result = float("inf")
        while high>=low:
            mid = low + ((high - low)// 2)
            if findCapacity(mid):
                result = min (result , mid)
                high = mid - 1
            else:
                low = mid +1
        return result
                
                
        