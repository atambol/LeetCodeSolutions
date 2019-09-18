class Solution {
    public String longestPalindrome(String s) {
        // new solution using DP
        // create a 2D array to store results
        int len = s.length();
        
        // edge cases
        if (len <= 1) {
            return s;
        }
        
        String sol = new String("");
        Integer[][] dp = new Integer[len][len];
        for(int i = 0; i < len; i++) {
            for(int j = 0; j < len; j++) {
                dp[i][j] = 0;
            }
        }
        
        // initialise all trivial solutions of size 1 and subsequently 2
        // 1 implies palindrome at <i,j> position while 0 implies otherwise
        for(int i = 0; i < len; i++) {
            dp[i][i] = 1;
        }
        sol = s.substring(0, 1);
        
        for(int i = 0; i < len-1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                dp[i][i+1] = 1;
                sol = s.substring(i, i+2);
            }
        }
        
        // build complex solutions on top of existing solutions
        // look at diagonally opposite cell to see if solution exists
        // if yes, check if a bigger solution is possible around it
         for(int i = 2; i < len; i++) {
            for(int j = i; j < len; j++) {
                if (dp[j-i+1][j-1] == 1 && s.charAt(j) == s.charAt(j-i)) {
                    dp[j-i][j] = 1;
                    sol = s.substring(j-i, j+1);
                }
            }
        }
        return sol;
    }
}
