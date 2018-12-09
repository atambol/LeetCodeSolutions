class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        sol = []
        count = 0
        for i in range(len(S)-1, -1, -1):
            s = S[i]
            if s == '-':
                continue
            elif 48 <= ord(s) <= 57:
                sol.append(s)
                count += 1
            elif 97 <= ord(s) <= 122:
                sol.append(chr(ord(s)-32))
                count += 1
            else:
                sol.append(s)
                count += 1
            if count != 0 and count%K == 0:
                sol.append("-")

        if sol and sol[-1] == '-':
            sol = sol[:-1]
        
        return "".join(sol[::-1])
            
        
