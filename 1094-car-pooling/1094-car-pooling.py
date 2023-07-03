class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeStamp = []
        for t in trips:
            timeStamp.append([t[1], t[0]])
            timeStamp.append([t[2], -t[0]])
        timeStamp.sort()
        
        usedSeats = 0
        for t, p in timeStamp:
            usedSeats += p
            if usedSeats > capacity:
                return False
        return True

        
        
        
        