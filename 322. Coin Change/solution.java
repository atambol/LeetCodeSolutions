class Solution {
    public int coinChange(int[] coins, int amount) {
        if (coins.length == 0) {
            return -1;
        }
        
        if (amount == 0) {
            return 0;
        }
        
        Arrays.sort(coins);
        int[] dp = new int[amount + 1];
        if (coins[0] > amount) {
            return -1;
        }
                
        int minValue;
        int i = 0;
        dp[0] = 0;
        i++;
        
        while (i < coins[0]) {
            dp[i] = 0;
            i++;
        }
        
        while (i <= amount) {
            minValue = Integer.MAX_VALUE;
            for (int j = 0; j < coins.length; j++) {
                if (i - coins[j] == 0) {
                    minValue = 1;
                }
                if (i - coins[j] > 0 && dp[i - coins[j]] > 0) {
                    minValue = Math.min(minValue, dp[i - coins[j]] + 1);
                }
            }
            if (minValue == Integer.MAX_VALUE) {
                dp[i] = -1;
            } else {
                dp[i] = minValue;
            }
            i++;
        }
        
        return dp[i-1];
    }
}
