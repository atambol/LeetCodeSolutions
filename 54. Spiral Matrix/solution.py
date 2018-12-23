class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        
        # edge case
        if not matrix:
            return spiral

        # maintain a map of direction to transition
        direction = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }
        
        # visited set of i,j indices
        visited = set()
        d = (0, 1)
        i = 0
        j = 0
        
        # total number of visited indices
        count = len(matrix) * len(matrix[0])
        
        # loop until all indices are not visited
        while len(visited) < count:
            # loop until the indices are valid and unvisited
            while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (i, j) not in visited:
                spiral.append(matrix[i][j])
                visited.add((i,j))
                i += d[0]
                j += d[1]
            
            # go back one step
            i -= d[0]
            j -= d[1]
            
            # get new direction
            d = direction[d]
            
            # change direction
            i += d[0]
            j += d[1]
        return spiral
