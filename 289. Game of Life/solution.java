class Solution {
    private int alive = 1;
    private int dead = 0;
    private int wasAliveNowAlive = 3;
    private int wasAliveNowDead = 5;
    private int wasDeadNowAlive = 2;
    private int wasDeadNowDead = 4;
    
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        int liveCount;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                liveCount = getLiveCount(board, i, j);
                if (board[i][j] == alive) {
                    if (liveCount == 2 || liveCount == 3) {
                        board[i][j] = wasAliveNowAlive;
                    } else {
                        board[i][j] = wasAliveNowDead;
                    }
                } else {
                    if (liveCount == 3) {
                        board[i][j] = wasDeadNowAlive;
                    } else {
                        board[i][j] = wasDeadNowDead;
                    }
                }
            }
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] < 4) {
                    board[i][j] = alive;
                } else {
                    board[i][j] = dead;
                }
            }
        }
    }
    
    public int getLiveCount(int[][] board, int i, int j) {
        int count = 0;
        int m = board.length;
        int n = board[0].length;
        if (i - 1 >= 0) {
            count += board[i-1][j] % 2;
        } 
        
        if (j - 1 >= 0) {
            count += board[i][j-1] % 2;
        }
        
        if (i + 1 < m) {
            count += board[i+1][j] % 2;
        }
        
        if (j + 1 < n) {
            count += board[i][j+1] % 2;
        }
        
        if (i - 1 >= 0 && j - 1 >= 0) {
            count += board[i-1][j-1] % 2;
        } 
        
        if (i + 1 < m && j - 1 >= 0) {
            count += board[i+1][j-1] % 2;
        }
        
        if (i + 1 < m  && j + 1 < n) {
            count += board[i+1][j+1] % 2;
        }
        
        if (i - 1 >= 0 && j + 1 < n) {
            count += board[i-1][j+1] % 2;
        }
        
        return count;
    }
}
