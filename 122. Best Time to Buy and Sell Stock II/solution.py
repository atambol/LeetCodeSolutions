class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) > 1:
            if len(prices) == 2:
                if prices[0] < prices[1]:
                    return prices[1] - prices[0]

            minprice = prices[0]
            for i in range(1, len(prices)):
                if prices[i] >= prices[i-1]:
                    continue
                else:
                    if minprice < prices[i-1]:
                        profit += prices[i-1] - minprice
                    minprice = prices[i]
            if prices[-1] - minprice > 0:
                profit += prices[-1] - minprice
                
        return profit
