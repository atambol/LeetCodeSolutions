class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        
        // edge cases
        if (prices.length < 2) 
            return profit;
            
        int i = 0;
        int minPrice = prices[i];
        i++;
        
        while (i < prices.length) {
            if (prices[i] < prices[i-1] && prices[i-1] > minPrice) {
                profit += prices[i-1] - minPrice;
                minPrice = prices[i];
            }
            minPrice = Math.min(prices[i], minPrice);
            i++;
        }
        
        if (minPrice < prices[i-1]) {
            profit += prices[i-1] - minPrice;
        }
        
        return profit;
    }
}
