class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TRACK MIN
        min_price = float('inf')
        best = 0
        # PROFIT
        for price in prices:
            profit = price - min_price
            # UPDATE BEST
            best = max(best, profit)
            # UPDATE MIN
            min_price = min(min_price, price)
        return best

        
        