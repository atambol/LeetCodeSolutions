class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int profit = 0;
        int minStock = prices[0];
        
        for (int i = 1; i < prices.length; i++) {
            minStock = Math.min(minStock, prices[i]);
            profit = Math.max(profit, prices[i] - minStock);
        }
        
        return profit;
    }
}
