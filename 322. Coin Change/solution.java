class Solution {
    public int coinChange(int[] coins, int amount) {
        Set<Integer> coinSet = new HashSet<Integer>();
        Arrays.sort(coins);
        int[] dp = new int[amount+1];
        
        for (int i = 1; i < amount+1; i++) {
            int maxCoins = Integer.MAX_VALUE;
            for (int coin: coins) {
                if (i - coin >= 0 && dp[i-coin] >= 0) {
                    maxCoins = Math.min(maxCoins, dp[i-coin] + 1);
                } else if (i - coin < 0) {
                    break;
                }
            }
            if (maxCoins == Integer.MAX_VALUE) {
                dp[i] = -1;
            } else {
                dp[i] = maxCoins;
            }
        }
        
        return dp[amount];
    }
}
