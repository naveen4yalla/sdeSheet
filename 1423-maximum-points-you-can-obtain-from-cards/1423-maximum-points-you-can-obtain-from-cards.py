class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        left = 0
        totalSum = sum(cardPoints[len(cardPoints) - k :])
        result = totalSum
        right = len(cardPoints) - k
        while len(cardPoints)>right:
            totalSum += cardPoints[left] - cardPoints[right]
            left = left + 1
            right = right + 1
            result = max(totalSum,result)
        return result 
        
                
        