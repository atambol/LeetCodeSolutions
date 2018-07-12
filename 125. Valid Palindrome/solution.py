class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        alnums = "abcdefghijklmnopqrstuvwxyz0123456789"
        
        string = "".join([t for t in s if t in alnums])
        i = 0
        j = len(string) -1
        
        if string == string[::-1]:
            return True
        else:
            return False
