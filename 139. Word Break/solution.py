class Solution:
    def __init__(self):
        self.visited = None
        self.maxsize = 0
        self.words = None
        
    def dfs(self, s, i):
        # all words found
        if i == len(s):
            return True
        
        # visited list
        if self.visited[i]:
            return False
        
        # mark visited
        self.visited[i] = True
        
        for j in range(i+1, i + self.maxsize + 1):
            if j > len(s):
                return False
            
            if s[i:j] in self.words:
                sol = self.dfs(s, j)
                if sol:
                    return True

        return False
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        
        # edge case
        if not n:
            return False
        
        # get the max size of the dictionary
        for w in wordDict:
            self.maxsize = max(self.maxsize, len(w))
            
        # create a dictionary from the list of words
        self.words = set(wordDict)
        
        # visited set to improve performance
        self.visited = [False]*n
        
        # perform dfs
        return self.dfs(s, 0)
