class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = []
        for S in s.split():
            t.append(S[::-1])
        return " ".join(t)
        
