class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # edge case
        peri = 0
        if not grid or not grid[0]:
            return peri
        
        # traverse the grid
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i-1][j] == 0:
                        peri += 1
                    
                    if j - 1 < 0 or grid[i][j-1] == 0:
                        peri += 1
                        
                    if j + 1 >= n or grid[i][j+1] == 0:
                        peri += 1
                        
                    if i + 1 >= m or grid[i+1][j] == 0:
                        peri += 1
                        
        return peri
