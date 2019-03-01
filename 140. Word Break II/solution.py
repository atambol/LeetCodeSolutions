class Solution:
    def __init__(self):
        self.unvisited = 0
        self.found = 1
        self.block = 2
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sol = []
        
        # handle edge cases
        if not s or not wordDict:
            return sol
        
        # add words to trie
        words = set(wordDict)
        visited = [self.unvisited]*len(s)
        
        # basic dfs
        return self.dfs(s, 0, words, visited)
    
    def dfs(self, s, i, words, visited):
        if visited[i] == self.block:
            return []
        
        sol = []
        j = i
        while j < len(s):
            if s[i:j+1] in words:
                if j + 1 == len(s):
                    sol.append(s[i:j+1])
                else:
                    subsol = self.dfs(s, j+1, words, visited)
                    for sub in subsol:
                        sol.append(" ".join([s[i:j+1], sub]))     
            j += 1
            
        if sol:
            visited[i] = self.found
        else:
            visited[i] = self.block
            
        return sol
