class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        sol = []
        if not s:
            return sol
        
        l = len(s)
        for i in range(0, l):
            if not s[:i+1] or int(s[:i+1]) > 255 or (s[:i+1][0] == "0" and len(s[:i+1]) > 1):
                break
            else:
                for j in range(i+1, l):
                    if not s[i+1:j+1] or int(s[i+1:j+1]) > 255 or (s[i+1:j+1][0] == "0" and len(s[i+1:j+1]) > 1):
                        break
                    else:
                        for k in range(j+1, l):
                            if not s[j+1:k+1] or int(s[j+1:k+1]) > 255 or (s[j+1:k+1][0] == "0" and len(s[j+1:k+1]) > 1):
                                break
                            else:
                                if not s[k+1:] or int(s[k+1:]) > 255 or (s[k+1:][0] == "0" and len(s[k+1:]) > 1):
                                    pass
                                else:
                                    ip = s[:i+1] + "." +\
                                         s[i+1:j+1] + "." +\
                                         s[j+1:k+1] + "." +\
                                         s[k+1:]
                                    sol.append(ip)
        return sol
