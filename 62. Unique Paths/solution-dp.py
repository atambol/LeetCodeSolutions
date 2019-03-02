class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # edge 
        if not m or not n:
            return 0
        
        # construct the matrix
        matrix = []
        for i in range(m):
            matrix.append([0]*n)
        matrix[0][0] = 1    
        
        for i in range(1, m):
            matrix[i][0] = matrix[i-1][0]
            
        for i in range(1, n):
            matrix[0][i] = matrix[0][i-1]

        # dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

        return matrix[-1][-1]
