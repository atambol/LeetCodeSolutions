class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices:
            return profit
        
        minPrice = prices[0]
        for price in prices:
            profit = max(profit, price - minPrice)
            minPrice = min(minPrice, price)

        return profit
