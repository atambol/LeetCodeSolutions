class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if not s:
            return False
        l = len(s)
        memo = [True]*l
        wordDict = set(wordDict)
        def backtracker(start = 0):
            i = start+1
            while i <= l:
                if s[start:i] in wordDict:
                    if i == l:
                        return True
                    else:
                        if memo[i]:
                            res = backtracker(i)
                            if res == True:
                                return True
                            else:
                                memo[i] = False
                        else:
                            pass
                i+=1
            return False
                    
        return backtracker()
                    
            
        
