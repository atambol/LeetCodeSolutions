class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if prices:
            minPrice = prices[0]
            for price in prices[1:]:
                if minPrice < price:
                    profit = max(price - minPrice, profit)
                minPrice = min(minPrice, price)
                
        return profit
        
