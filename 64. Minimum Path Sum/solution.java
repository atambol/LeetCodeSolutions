class Solution {
    public int minPathSum(int[][] grid) {
        if (grid.length == 0) {
            return 0;
        }
        if (grid[0].length == 0) {
            return 0;
        }
        
        int[][] dp = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                dp[i][j] = 0;
            }
        }
        
        int minPath = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (i == 0 && j == 0) {
                    minPath = 0;
                } else if (i == 0 && j != 0) {
                    minPath = dp[i][j-1];
                } else if (i != 0 && j == 0) {
                    minPath = dp[i-1][j];
                } else {
                    minPath = Math.min(dp[i-1][j], dp[i][j-1]);
                }
                
                dp[i][j] = minPath + grid[i][j];
            }
        }
        
        return dp[grid.length-1][grid[0].length-1];
    }
}
