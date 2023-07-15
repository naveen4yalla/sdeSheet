class UndergroundSystem:

    def __init__(self):
        self.check = {}            
        self.totalTime = {} #key = (stationName,endStation) value = total time ,count
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start , time = self.check[id]
        route = (start,stationName)
        if route not in self.totalTime.keys():
            self.totalTime[route] =[0,0]
        self.totalTime[route][0] += t-time
        self.totalTime[route][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation,endStation)
        totalTime , count = self.totalTime[route]
        return totalTime/count
    
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)