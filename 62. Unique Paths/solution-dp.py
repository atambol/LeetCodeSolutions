class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # edge case
        if not m or not n:
            return 0
        
        # initialise the sol array 
        # the top most and left most row starts with 1
        # the rest of cells are calculated based on the cells to their left and top
        sol = []
        for i in range(m):
            s = []
            for j in range(n):
                if not i or not j:
                    s.append(1)
                else:
                    s.append(0)
            sol.append(s)
        
        # use dynamic programming to calculate the unique path count
        # in row major fashion, count the paths from left to right
        for i in range(1, m):
            for j in range(1, n):
                sol[i][j] = sol[i][j-1] + sol[i-1][j]
        
        # solution is in the last cell
        return sol[-1][-1]
