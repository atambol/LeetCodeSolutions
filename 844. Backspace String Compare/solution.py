class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = len(S) - 1
        t = len(T) - 1
        sb = 0
        tb = 0
        
        equal = True
        while equal:
            if s >= 0:
                if S[s] == "#":
                    s -= 1
                    sb += 1
                    continue
                elif sb > 0:
                    s -= 1
                    sb -= 1
                    continue
            
            if t >= 0:
                if T[t] == "#":
                    t -= 1
                    tb += 1
                    continue
                elif tb > 0:
                    t -= 1
                    tb -= 1
                    continue
            
            if s >= 0 and t >= 0:
                if S[s] == T[t]:
                    t -= 1
                    s -= 1
                else:
                    equal = False
            else:
                return s == t
                
        return equal
        
