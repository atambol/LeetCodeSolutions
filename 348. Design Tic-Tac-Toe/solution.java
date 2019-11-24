class TicTacToe {
    public int[][] board;
    public int size;
    
    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        size = n;
        board = new int[n][n];
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        board[row][col] = player;
        return checkWins(row, col);
    }
    
    public int checkWins(int row, int col) {
        boolean win = true;
        
        // check horizontally
        for (int i = 0; i < size; i++) {
            if (board[row][i] != board[row][col]) {
                win = false;
                break;
            }
        }
        
        if (win) {
            return board[row][col];
        }
        
        // check vertically
        win = true;
        for (int i = 0; i < size; i++) {
            if (board[i][col] != board[row][col]) {
                win = false;
                break;
            }
        }
        
        if (win) {
            return board[row][col];
        }
        
        // check diagonally
        if (col == row) {
            win = true;
            for (int i = 0; i < size; i++) {
                if (board[i][i] != board[row][col]) {
                    win = false;
                    break;
                }
            }
            if (win) {
                return board[row][col];
            }
        }
        if (col == size - row - 1) {
            win = true;
            for (int i = 0; i < size; i++) {
                if (board[i][size-i-1] != board[row][col]) {
                    win = false;
                    break;
                }
            }
            if (win) {
                return board[row][col];
            }
        }
        
        return 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
