class Solution {
    public int findCircleNum(int[][] M) {
        // edge case
        int circles = 0;
        int n = M.length;
        if (n == 0) {
            return circles;
        }
        
        // visited list
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            visited[i] = false;
        }
        
        // dfs on each friend
        for (int i = 0; i < n; i++) {
            if (visited[i] == false) {
                circles++;
                dfs(i, M, visited);
            }
        }
        return circles;
    }
    
    public void dfs(int i, int[][] M, boolean[] visited) {
        if (visited[i] == true) {
            return;
        }
        
        visited[i] = true;
        for (int j = 0; j < visited.length; j++) {
            if (M[i][j] == 1)
                dfs(j, M, visited);
        }
    }
}
