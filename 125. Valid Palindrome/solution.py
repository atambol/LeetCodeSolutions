class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        i = 0
        j = len(s) - 1
        
        while i < j:
            if not self.isAlnum(s[i]):
                i += 1
                continue

            if not self.isAlnum(s[j]):
                j -= 1
                continue
            else:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
                
        return True
            
        
    def isAlnum(self, c):
        o = ord(c)
        if 90 >= o >= 65 or 122 >= o >= 97 or 57 >= o >= 48:
            return True
        else:
            return False
