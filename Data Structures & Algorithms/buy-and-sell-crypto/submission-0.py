class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = 100

        for x in prices:
            low = min(low, x)
            profit = max(profit, x - low)

        return profit
        