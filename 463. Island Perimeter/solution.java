class Solution {
    public int islandPerimeter(int[][] grid) {
        int m = grid.length;
        if (m == 0) {
            return 0;
        }
        int n = grid[0].length;
        if (n == 0) {
            return 0;
        }
        
        boolean[][] visited = new boolean[m][n];
        int p = -1, q = -1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = false;
                if (grid[i][j] == 1 && p == -1) {
                    p = i;
                    q = j;
                }
            }
        }
        
        if (p == -1) 
            return 0;
        
        return dfs(p, q, grid, visited);
    }
    
    public int dfs(int i, int j, int[][] grid, boolean[][] visited) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == 0)
            return 1;
        
        if (visited[i][j])
            return 0;
        
        visited[i][j] = true;
        
        return dfs(i+1, j, grid, visited) + dfs(i-1, j, grid, visited) + dfs(i, j+1, grid, visited) + dfs(i, j-1, grid, visited);
            
    }
}
