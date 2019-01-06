class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # edge case
        profit = 0
        if not prices:
            return profit
        
        # dp
        minPrice = prices[0]
        
        for price in prices[1:]:
            if minPrice < price:
                profit += price - minPrice
                
            minPrice = price
            
        return profit
