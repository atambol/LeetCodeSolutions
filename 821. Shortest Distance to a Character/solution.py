class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        prev = None
        res = [sys.maxsize]*len(S)
        
        for i, s in enumerate(S):
            if s == C:
                prev = i
                res[i] = 0
            else:
                if prev != None:
                    res[i] = i - prev
        
        prev = None
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                prev = i
            else:
                if prev and prev - i < res[i]:
                    res[i] = prev - i
                    
        return res
