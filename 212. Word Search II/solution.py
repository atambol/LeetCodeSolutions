class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Variables used for complexity analysis:
        l: maximum length of a word
        w: number of words in the input list
        n: number of points on the board
        
        overall complexity: O(l*(w+n))
        """
        sol = []
        
        # edge cases - O(1)
        n = len(board)
        if not n:
            return sol
        m = len(board[0])
        if not m:
            return sol
        if not words:
            return sol
        
        # store words as a trie - O(w*l)
        size = n * m
        trie = {}
        for word in words:
            if len(word) > size:
                continue
            ptr = trie
            for w in word:
                if w not in ptr:
                    ptr[w] = {}
                ptr = ptr[w]
            ptr["#"] = "#"

        # dfs over each point on the board - O(n*l)
        sol = set()
        visited = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    self.dfs(board, i, j, visited, trie, sol, "")
                        
        return list(sol)
    
    # time complexity for dfs: O(l)
    def dfs(self, board, i, j, visited, trie, sol, prev):
        if "#" in trie:
            sol.add(prev)
            
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] not in trie:
            return
        
        if (i, j) in visited:
            return
        
        visited.add((i, j))
        
        self.dfs(board, i-1, j, visited, trie[board[i][j]], sol, prev + board[i][j])
        self.dfs(board, i, j-1, visited, trie[board[i][j]], sol, prev + board[i][j])
        self.dfs(board, i+1, j, visited, trie[board[i][j]], sol, prev + board[i][j])
        self.dfs(board, i, j+1, visited, trie[board[i][j]], sol, prev + board[i][j]) 
        
        visited.remove((i, j))
