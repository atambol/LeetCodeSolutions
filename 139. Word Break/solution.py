class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(wordDict)
        visited = [False]*len(s)
        return self.search(s, words, visited, 0)
    
    # basic dfs
    def search(self, s, words, visited, i):
        # check if the string is exhausted
        if i == len(s):
            return True
        
        # check if visited
        if visited[i]:
            return False
        
        # mark visited
        visited[i] = True
        j = i
        
        # dfs over the s
        while j < len(s):
            if s[i:j+1] in words:
                res = self.search(s, words, visited, j+1)
                if res:
                    return res
            j += 1
            
        return False
