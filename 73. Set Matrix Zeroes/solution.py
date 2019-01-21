class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k]:
                            matrix[i][k] = '#'
                            
                    for k in range(m):
                        if matrix[k][j]:
                            matrix[k][j] = '#'
                            
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
                            
