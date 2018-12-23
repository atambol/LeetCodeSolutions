class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # create a matrix to fill
        matrix = []
        for i in range(n):
            matrix.append([None]*n)
            
        # direction transition
        direction = {
            (0, 1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1)
        }
        
        visited = set()
        count = 1
        total = n*n
        d = (0,1)
        i = 0
        j = 0
        while count <= total:
            while 0 <= i < n and 0 <= j < n and (i, j) not in visited:
                visited.add((i,j))
                matrix[i][j] = count
                count += 1
                i += d[0]
                j += d[1]
                
            # go back one
            i -= d[0]
            j -= d[1]
            
            # get new direction
            d = direction[d]
            
            # change direction
            i += d[0]
            j += d[1]
            
        return matrix
                        
