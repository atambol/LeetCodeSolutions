class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if not n:
            return 
        
        m = len(matrix[0])
        if not m:
            return
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    self.mark(matrix, i, j, n, m)
                    
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
                    
        
    def mark(self, matrix, x, y, n, m):
        for i in range(n):
            if matrix[i][y] != 0:
                matrix[i][y] = "#"
        
        for i in range(m):
            if matrix[x][i] != 0:
                matrix[x][i] = "#"
                
                
