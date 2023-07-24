from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.pts = defaultdict(int)
        self.p = []

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1
        self.p.append(point)

    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        result = 0
        for xp, yp in self.p:  # Convert the dictionary items to a list before iterating
            if (abs(xp - x) != abs(yp - y)) or x == xp or y == yp:
                continue
            result += self.pts[(x, yp)] * self.pts[(xp, y)]
        return result


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)