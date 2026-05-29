class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        minBuy = prices[0]
        for i in range(len(prices)):
            profit = max(profit, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])
        return profit
