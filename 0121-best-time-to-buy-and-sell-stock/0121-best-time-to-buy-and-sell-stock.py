class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif (prices[i] - mini > maxprofit):
                maxprofit = prices[i] - mini
        return maxprofit
        