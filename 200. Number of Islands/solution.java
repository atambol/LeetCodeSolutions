class Solution {
    public int numIslands(char[][] grid) {
        // edge cases
        int m = grid.length;
        if (m == 0) {
            return 0;
        }
        
        int n = grid[0].length;
        if (n == 0) {
            return 0;
        }
        
        // count islands using dfs
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j, m, n);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    public void dfs(char[][] grid, int i, int j, int m, int n) {
        if (i >= 0 && i < m && j >= 0 && j < n && grid[i][j] == '1') {
            grid[i][j] = '#';
            dfs(grid, i-1, j, m, n);
            dfs(grid, i, j-1, m, n);
            dfs(grid, i, j+1, m, n);
            dfs(grid, i+1, j, m, n);
        }
    }
}
