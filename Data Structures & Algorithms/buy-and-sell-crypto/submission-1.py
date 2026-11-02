class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                maxP = max(maxP, p)
            else:
                l = r
            
            r += 1
        
        return maxP