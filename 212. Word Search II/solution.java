class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        List<String> sol = new ArrayList<String>();
        
        int m = board.length;
        if (m == 0) {
            return sol;
        }
        int n = board[0].length;
        if (n == 0) {
            return sol;
        }
        
        boolean found;
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (String word: words) {
            found = false;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (word.charAt(0) == board[i][j] && dfs(board, i, j, word, 0, visited)) {
                        sol.add(word);
                        found = true;
                        break;
                    }
                }
                if (found)
                    break;
            }
        }
        return sol;
    }
    
    public boolean dfs(char[][] board, int i, int j, String word, int k, boolean[][] visited) {
        if (k == word.length()) {
            return true;
        }
        
        if (i >= 0 && j >= 0 && i < board.length && j < board[0].length && 
            !visited[i][j] && board[i][j] == word.charAt(k)) {
            visited[i][j] = true;
            boolean res = dfs(board, i+1, j, word, k+1, visited) ||
            dfs(board, i, j+1, word, k+1, visited) ||
            dfs(board, i, j-1, word, k+1, visited) ||
            dfs(board, i-1, j, word, k+1, visited);
            visited[i][j] = false;
            return res;
        } else {
            return false;
        }
    }
}
