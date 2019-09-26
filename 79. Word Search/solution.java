class Solution {
    public boolean exist(char[][] board, String word) {        
        //edge cases
        if (board.length == 0 || board[0].length == 0) {
            return false;
        }
        
        if (word.length() == 0) {
            return false;
        }
        
        // allocate visited grid
        int[][] visited = new int[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                visited[i][j] = 0;
            }
        }
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (word.charAt(0) == board[i][j]) {
                    // System.out.printf("%d, %d, %c \n", i, j, board[i][j]);
                    if (dfs(board, i, j, word, 0, visited)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    public boolean dfs(char[][] board, int i, int j, String word, int k, int[][] visited) {
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length || 
            board[i][j] != word.charAt(k) || 
            visited[i][j] == 1) {
            return false;
        }
        
        if (k == word.length()-1) {
            return true;
        }
        
        visited[i][j] = 1;
        boolean found = dfs(board, i-1, j, word, k+1, visited) ||
            dfs(board, i, j-1, word, k+1, visited) ||
            dfs(board, i+1, j, word, k+1, visited) ||
            dfs(board, i, j+1, word, k+1, visited);
        visited[i][j] = 0;
        return found;
    }
}
