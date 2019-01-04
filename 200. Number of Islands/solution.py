class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid, i, j):
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '-1'
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j-1)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i+1, j)
            
