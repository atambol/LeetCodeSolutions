class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                num += self.dfs(grid, i, j)
        return num
        
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] in ['-1', '0']:
            return 0
        else:
            grid[i][j] = '-1'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
            return 1
