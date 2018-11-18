class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) > 1:
            # edge case of 2 elements only
            if len(prices) == 2:
                if prices[0] < prices[1]:
                    return prices[1] - prices[0]

            # for number of elements greater than 2
            minprice = prices[0]
            for i in range(1, len(prices)):
                # Keep looking for the next peak
                if prices[i] >= prices[i-1]:
                    continue
                else:
                    # once the peak starts to fall, calculate the local profit and update the minprice
                    if minprice < prices[i-1]:
                        profit += prices[i-1] - minprice
                    minprice = prices[i]
            # check for the last element if it was a peak
            if prices[-1] - minprice > 0:
                profit += prices[-1] - minprice
                
        return profit
