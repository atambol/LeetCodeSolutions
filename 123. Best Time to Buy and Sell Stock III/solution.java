class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) 
            return 0;
        
        int minPrice;
        int maxPrice;
        int profit;
        int[] lp = new int[prices.length];
        int[] rp = new int[prices.length];
        minPrice = prices[0];
        profit = 0;
        
        lp[0] = 0;
        minPrice = prices[0];
        for (int i = 1; i < prices.length; i++) {
            minPrice = Math.min(minPrice, prices[i]);
            profit = prices[i] - minPrice;
            lp[i] = Math.max(profit, lp[i-1]);
        }
        
        rp[prices.length-1] = 0;
        profit = 0;
        maxPrice = prices[prices.length-1];
        for (int i = prices.length - 2; i >= 0; i--) {
            maxPrice = Math.max(maxPrice, prices[i]);
            profit = maxPrice - prices[i];
            rp[i] = Math.max(profit, rp[i+1]);
        }
        
        profit = 0;
        for (int i = 0; i < prices.length; i++) {
            profit = Math.max(profit, lp[i] + rp[i]);
        }
        
        return profit;
    }
}
