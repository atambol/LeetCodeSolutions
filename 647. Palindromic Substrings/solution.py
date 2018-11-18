class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge cases
        if not s:
            return 0
        
        # count all the basic palindromic substrings
        l = len(s)
        count = l
        
        # use the expand around the center technique
        # start counting the palindromes starting with each index
        for i in range(len(s)):
            j = i-1
            k = i+1
            while j >= 0 and k < l and s[k] == s[j]:
                count += 1
                j -= 1
                k += 1
            
        # start counting the palindromes starting between two index
        for i in range(len(s)-1):
            j = i
            k = i+1
            while j >= 0 and k < l and s[k] == s[j]:
                count += 1
                j -= 1
                k += 1
                
        return count
