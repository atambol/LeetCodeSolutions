class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # edge case
        if not s or not wordDict:
            return False
        
        # create word set
        words = set(wordDict)
        
        # basic dfs
        visited = [False]*len(s)
        return self.dfs(words, visited, s, 0)
    
    def dfs(self, words, visited, string, start):
        if visited[start]:
            return False
        
        visited[start] = True
        
        for end in range(start, len(string)):
            if string[start:end+1] in words:
                if end == len(string) - 1:
                    return True
                else:
                    res = self.dfs(words, visited, string, end+1)
                    if res:
                        return True
                    
        return False
            
