class Solution:
    def countOdds(self, low: int, high: int) -> int:
        len = high - low + 1
        count = len // 2
        if len % 2 and low % 2:
            return count + 1
        return count
    
        