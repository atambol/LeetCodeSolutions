class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # edge cases
        if not board or not word:
            return False
        
        # perform dfs on every cell with starting letter of word
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                visited = set()
                res = self.dfs(board, i, j, word, 0, visited, m, n)
                if res:
                    return True
        return False
    
    def dfs(self, board, i, j, word, k, visited, m, n):
        # check if within range
        if 0 <= i < n and 0 <= j < m and (i, j) not in visited and board[i][j] == word[k]:
            # check if end of word
            k += 1
            if k == len(word):
                return True
        
            # keep doing dfs
            visited.add((i, j))
            res = False
            res = res or self.dfs(board, i+1, j, word, k, visited, m, n)
            res = res or self.dfs(board, i-1, j, word, k, visited, m, n)
            res = res or self.dfs(board, i, j+1, word, k, visited, m, n)
            res = res or self.dfs(board, i, j-1, word, k, visited, m, n)
            visited.remove((i, j))
            return res
        
        return False
