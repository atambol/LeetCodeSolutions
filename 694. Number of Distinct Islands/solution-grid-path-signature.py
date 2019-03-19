class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # edge cases
        if not grid or not grid[0]:
            return 0
        
        signatures = set()
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    signature = []
                    self.dfs(grid, i, j, visited, 0, signature)
                    signatures.add(tuple(signature))
                    
        return len(signatures)
    
    def dfs(self, grid, i, j, visited, key, signature):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 0:
            return
        
        visited.add((i, j))
        signature.append(key)
        self.dfs(grid, i+1, j, visited, 1, signature)
        self.dfs(grid, i-1, j, visited, 2, signature)
        self.dfs(grid, i, j-1, visited, 3, signature)
        self.dfs(grid, i, j+1, visited, 4, signature)
        signature.append(0)
    
