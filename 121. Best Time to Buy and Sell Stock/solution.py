class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        # maintain a minprice and maxprice array
        minprice = [None]*len(prices)
        minprice[0] = prices[0]
        maxprice = [None]*len(prices)
        maxprice[-1] = prices[-1]
        
        # populate the min prices and maxprices
        for i in range(1, len(prices)):
            minprice[i] = min(minprice[i-1], prices[i])
        for i in range(len(prices)-2, -1, -1):
            maxprice[i] = max(maxprice[i+1], prices[i])
           
        # calculate the maxprofit
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, maxprice[i] - minprice[i])
            
        return profit
