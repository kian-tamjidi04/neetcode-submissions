class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Using sliding window
        res = 0
        bestBuy = prices[0] # Best price to buy the stock at

        for price in prices:
            # Update best price if we have found lower price to buy
            if price < bestBuy:
                bestBuy = price
            res = max(res, price - bestBuy)
        
        return res