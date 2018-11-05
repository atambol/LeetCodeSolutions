class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # print(s)
        memo = set()
        return self.memoWordBreak(s, wordDict, memo)
        

    def memoWordBreak(self, s, wordDict, memo):
        """
        :type s: str
        :type wordDict: List[str]
        :type memo: set
        :rtype: bool
        """
        for i in range(1, len(s)+1):
            if s[:i] in wordDict:
                if i == len(s):
                    return True
                else:
                    index = len(s) + 1 - i
                    if index in memo:
                        continue
                    else:
                        if self.memoWordBreak(s[i:], wordDict, memo):
                            return True
                        else:
                            memo.add(index)
                    
        return False
              
