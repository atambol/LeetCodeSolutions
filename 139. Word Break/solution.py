class Solution:
    def __init__(self):
        self.visited = []
        self.maxSize = 0
        self.words = set()
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # visited list
        self.visited = [False]*len(s)
        
        # calculate the maxsize of a word
        for w in wordDict:
            self.maxSize = max(self.maxSize, len(w))
        
        # O(n) lookup for a word
        self.words.update(wordDict)
        
        return self.myWordBreak(s, 0)
        
    def myWordBreak(self, s, i):
        # base condition
        if i == len(s):
            return True
        
        # visited array - memoization
        if self.visited[i]:
            return False
        
        # mark i visited
        self.visited[i] = True
        
        # calculate the limit of the word
        l = min(i + self.maxSize + 1, len(s)+1)
        
        # check if word in set
        for j in range(i+1, l):
            if s[i:j] in self.words:
                isBreak = self.myWordBreak(s, j)
                if isBreak:
                    return True
                
        return False
        
