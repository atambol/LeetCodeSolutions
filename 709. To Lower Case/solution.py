class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        string = []
        for s in str:
            if 64 < ord(s) < 92:
                string.append(chr(ord(s) + 32))
            else:
                string.append(s)
                
        return "".join(string)
