class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyprice = float('inf')
        for p in prices:
            if p < buyprice:
                buyprice = p
            else:
                profit = max(profit, p - buyprice)
        return profit

