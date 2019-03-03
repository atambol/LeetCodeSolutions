class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0
        
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i - 1 >= 0:
                    grid[i][j] += grid[i-1][j]
                elif j - 1 >= 0:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]
