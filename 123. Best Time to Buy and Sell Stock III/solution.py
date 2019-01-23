class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # edge cases
        if len(prices) < 2:
            return 0
        
        # calculate profits from left side
        leftprofits = [0]
        minprice = prices[0]
        for price in prices[1:]:
            minprice = min(price, minprice)
            profit = price - minprice
            maxprofit = max(leftprofits[-1], profit)
            leftprofits.append(profit)

        # calculate profits from right side
        rightprofits = [0]
        maxprice = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            maxprice = max(prices[i], maxprice)
            profit = maxprice - prices[i]
            maxprofit = max(profit, rightprofits[-1])
            rightprofits.append(maxprofit)
        rightprofits.reverse()

        # calculate the maxmimum profits from both sides
        maxprofit = 0
        for i, j in zip(leftprofits, rightprofits):
            maxprofit = max(maxprofit, i+j)
            
        return maxprofit
            
                
