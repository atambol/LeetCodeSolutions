class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = len(grid)
        y = len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < x and 0 <= j < y and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
            else:
                return 0
            
        maxArea = 0
        for m in range(x):
            for n in range(y):
                area = dfs(m, n)
                if area > maxArea:
                    maxArea = area
                    
        return maxArea
