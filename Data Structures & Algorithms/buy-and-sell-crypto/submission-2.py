class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyprice = float('inf')
        # consider selling every day, the max profit possible on that day is based on the lowest price observed anytime in the past
        for p in prices:
            if p < buyprice:
                buyprice = p
            else:
                profit = max(profit, p - buyprice)
        return profit

