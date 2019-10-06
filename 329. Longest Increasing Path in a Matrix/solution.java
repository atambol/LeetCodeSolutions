class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length;
        if (m == 0) {
            return 0;
        }
        
        int n = matrix[0].length;
        if (n == 0) {
            return 0;
        }
        
        int[][] memo = new int[m][n];
        for (int i = 0; i < m; i++) {
           for (int j = 0; j < n; j++) {
               memo[i][j] = 1;
           }
        }
        
        int maxLen = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (memo[i][j] == 1) {
                    maxLen = Math.max(dfs(matrix, i, j, m, n, memo), maxLen);
                }
            }
        }
        
        return maxLen;
    }
    
    private int dfs(int[][] matrix, int i, int j, int m, int n, int[][] memo) {        
        if (isValid(i-1, j, m, n) && (matrix[i-1][j] < matrix[i][j])) {
            if (memo[i-1][j] == 1) {
                dfs(matrix, i-1, j, m, n, memo);
            }
            memo[i][j] = Math.max(memo[i][j], memo[i-1][j]+1);
        } 
        
        if (isValid(i+1, j, m, n) && (matrix[i+1][j] < matrix[i][j])) {
            if (memo[i+1][j] == 1) {
                dfs(matrix, i+1, j, m, n, memo);
            }
            memo[i][j] = Math.max(memo[i][j], memo[i+1][j]+1);
        }
        
        if (isValid(i, j-1, m, n) && (matrix[i][j-1] < matrix[i][j])) {
            if (memo[i][j-1] == 1) {
                dfs(matrix, i, j-1, m, n, memo);
            }
            memo[i][j] = Math.max(memo[i][j], memo[i][j-1]+1);
        }
        
        if (isValid(i, j+1, m, n) && (matrix[i][j+1] < matrix[i][j])) {
            if (memo[i][j+1] == 1) {
                dfs(matrix, i, j+1, m, n, memo);
            }
            memo[i][j] = Math.max(memo[i][j], memo[i][j+1]+1);
        }
        return memo[i][j];
    }
    
    public boolean isValid(int x, int y, int m, int n) {
        return ((x >= 0) && (x < m) && (y >= 0) && (y < n));
    }
}
