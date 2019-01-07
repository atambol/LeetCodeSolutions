class Solution:
    def __init__(self):
        # direction transition
        self.nextDir = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }
        
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        sol = []
        
        # edge case
        if not matrix or not matrix[0]:
            return sol
        
        # starting points and direction
        i = 0
        j = 0
        dir = (0, 1)
        
        # constraints
        seen = set()
        m = len(matrix)
        n = len(matrix[0])
        count = m*n
        
        # spiral in
        while len(seen) != count:
            # change direction if constrained
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in seen:
                i = i-dir[0]
                j = j-dir[1]
                
                dir = self.nextDir[dir]
                i = i+dir[0]
                j = j+dir[1]    
            
            # record the spiral and mark the cells seen
            sol.append(matrix[i][j])
            seen.add((i, j))
            
            # next cell
            i = i+dir[0]
            j = j+dir[1] 
            
        return sol
