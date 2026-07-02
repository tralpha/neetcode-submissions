class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TRACK MIN
        min_price = float('inf')
        best = 0
        for price in prices:
            # PROFIT
            profit = price - min_price
            # UPDATE BEST PROFIT
            best = max(best, profit)
            # UPDATE MIN PRICE
            min_price = min(min_price, price)
        return best


        