class Solution:
    def __init__(self):
        self.r2i = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000,
        }

    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = len(s)
        i = 0
        while i < l:
            if i+1 < l:
                a = self.r2i[s[i]]
                b = self.r2i[s[i+1]]
                if a < b:
                    res += b-a
                    i += 1
                else:
                    res += a
                
            else:
                res += self.r2i[s[i]]
            i += 1
        return res
