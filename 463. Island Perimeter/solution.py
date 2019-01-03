class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i-1 >= 0:
                        if grid[i-1][j] == 0:
                            count += 1
                    else:
                        count += 1
                    
                    if i+1 < m:
                        if grid[i+1][j] == 0:
                            count += 1
                    else:
                        count += 1
                        
                    if j-1 >= 0:
                        if grid[i][j-1] == 0:
                            count += 1
                    else:
                        count += 1
                    
                    if j+1 < n:
                        if grid[i][j+1] == 0:
                            count += 1
                    else:
                        count += 1
                    
        return count            
