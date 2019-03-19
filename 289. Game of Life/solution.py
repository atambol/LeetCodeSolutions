class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                self.check(board, i, j)
                
        for i in range(n):
            for j in range(m):
                self.update(board, i, j)
    
    def update(self, board, i, j):
        if board[i][j] == 2:
            board[i][j] = 1
        elif board[i][j] == 3:
            board[i][j] = 0
                
    def check(self, board, i, j):
        count_neigh = 0
        neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), 
                    (i, j-1), (i, j+1),
                    (i+1, j-1), (i+1, j), (i+1, j+1)]
        
        n = len(board)
        m = len(board[0])
        for x, y in neighbors:
            if x < 0 or y < 0 or x >= n or y >= m:
                continue
            if board[x][y] % 2 == 1:
                count_neigh += 1
        
        if board[i][j] == 0:
            if count_neigh == 3:
                board[i][j] = 2
        else:
            if count_neigh < 2 or count_neigh > 3:
                board[i][j] = 3
