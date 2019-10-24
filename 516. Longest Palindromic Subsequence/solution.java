class Solution {
    public int longestPalindromeSubseq(String s) {
        if (s.length() < 2) {
            return s.length();
        }
        int[][] dp = new int[s.length()][s.length()];
        
        for (int i = 0; i < s.length(); i++) {
            dp[i][i] = 1;
        }
        
        for (int i = s.length(); i >= 0; i--) {
            for (int j = i + 1; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = 2 + dp[i+1][j-1];
                } else {
                    dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        
        return dp[0][s.length()-1];
    }
}
