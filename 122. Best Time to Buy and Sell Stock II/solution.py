class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        # edge cases
        if not prices or len(prices) < 2:
            return profit

        # loop over each price
        # add to profit if previous price is less than current price
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
