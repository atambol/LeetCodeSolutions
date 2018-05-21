class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        for i,e in enumerate(str(abs(x))):
            if str(abs(x))[i] != str(x)[len(str(abs(x)))-i-1]:
                return False
        return True
