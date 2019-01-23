class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dir = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }
        
        sol = []
        m = len(matrix)
        if not m:
            return sol
        n = len(matrix[0])
        if not n:
            return sol
        
        x, y = 0, 1
        i, j = 0, 0
        visited = set()
        count = m*n
        while count:
            while i >= 0 and j >= 0 and i < m and j < n and (i, j) not in visited:
                visited.add((i, j))
                sol.append(matrix[i][j])
                count -= 1
                i += x
                j += y
            i -= x
            j -= y
            x, y = dir[(x, y)]
            i += x
            j += y
            
        return sol
