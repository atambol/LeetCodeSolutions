class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        
        # edge cases
        if not grid or not grid[0]:
            return 0
        
        signatures = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    signature = self.dfs(grid, i, j, visited)
                    if signature:
                        signatures.add(self.rescale(signature))
                    
        return len(signatures)
    
    def rescale(self, signature):
        new = []
        min_i = min(signature, key=lambda x: x[0])[0]
        min_j = min(signature, key=lambda x: x[1])[1]
        for i, j in signature:
            new.append((i-min_i, j-min_j))
        return tuple(new)
    
    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 0:
            return []
        
        visited.add((i, j))
        signature = []
        signature.extend(self.dfs(grid, i-1, j, visited))
        signature.extend(self.dfs(grid, i, j-1, visited))
        signature.append((i, j))
        signature.extend(self.dfs(grid, i, j+1, visited))
        signature.extend(self.dfs(grid, i+1, j, visited))
        return signature
    
