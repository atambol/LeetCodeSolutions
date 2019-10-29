class Solution {
    public void solve(char[][] board) {
        // edge cases
        int m = board.length;
        if (m == 0) {
            return;
        }
        int n = board[0].length;
        if (n == 0) {
            return;
        }

        // visit edges and mark uncapturable regions with U
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') {
                mark(board, 0, j);
            }
            if (board[m-1][j] == 'O') {
                mark(board, m-1, j);
            }
        }
        
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') {
                mark(board, i, 0);
            }
            if (board[i][n-1] == 'O') {
                mark(board, i, n-1);
            }
        }
        
        // mark all O as X and all U as O
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'U') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }
    
    public void mark(char[][] board, int i, int j) {
        int m = board.length;
        int n = board[0].length;
        if (i >= m || i < 0 || j >= n || j < 0 || board[i][j] == 'X' || board[i][j] == 'U') {
            return;
        }
        
        board[i][j] = 'U';

        mark(board, i-1, j);
        mark(board, i, j+1);
        mark(board, i+1, j);
        mark(board, i, j-1);
    }
}
