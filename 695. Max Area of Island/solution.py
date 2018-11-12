class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    if area > maxArea:
                        maxArea = area
                        
        return maxArea
                        
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != 1:
            return 0
        else:
            grid[i][j] = -1
            return 1 + \
                    self.dfs(grid, i + 1, j) + \
                    self.dfs(grid, i, j + 1) + \
                    self.dfs(grid, i, j - 1) + \
                    self.dfs(grid, i - 1, j)
