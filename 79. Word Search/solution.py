class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, visited, i, j, word, 0):
                        return True
        
        return False
        
    def dfs(self, board, visited, i, j, word, k):
        if k == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited or word[k] != board[i][j]:
            return False
        
        visited.add((i, j))
        res = self.dfs(board, visited, i-1, j, word, k+1) or \
              self.dfs(board, visited, i, j-1, word, k+1) or \
              self.dfs(board, visited, i+1, j, word, k+1) or \
              self.dfs(board, visited, i, j+1, word, k+1) 
        
        visited.remove((i, j))
        return res
    
        
