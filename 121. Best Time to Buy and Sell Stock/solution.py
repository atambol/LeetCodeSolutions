class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        # run through all possible cases
        profit = 0
        price = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - price)
            price = min(price, prices[i])
            
        return profit
