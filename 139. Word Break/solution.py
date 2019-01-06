class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        
        visited = [0]*len(s)
        return self.myWordBreak(s, 0, wordDict, visited)
    
    def myWordBreak(self, s, start, wordDict, visited):
        if start == len(s):
            return True
        
        if visited[start]:
            return False
        
        for i in range(start, len(s)):
            if s[start:i+1] in wordDict:
                canSegment = self.myWordBreak(s, i+1, wordDict, visited)
                if canSegment:
                    return True
                
        visited[start] = 1
        return False
        
        
