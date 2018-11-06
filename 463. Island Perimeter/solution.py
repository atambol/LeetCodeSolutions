class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        peri = 0
        for i in range(m):
            n = len(grid[i])
            for j in range(n):
                if grid[i][j] == 1:
                    neighbours = [[i,j+1],[i,j-1],[i-1,j],[i+1,j]]
                    for neighbour in neighbours:
                        if neighbour[0] >= m or neighbour[0] < 0 or neighbour[1] < 0 or neighbour[1] >= n:
                            peri += 1
                        else:
                            if grid[neighbour[0]][neighbour[1]] == 0:
                                peri += 1

        return peri
                            
