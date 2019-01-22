class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sol = ""
        
        # expand around index
        for i in range(len(s)):
            j = i - 1
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            
            j += 1
            k -= 1
            if k - j + 1 > len(sol):
                sol = s[j:k+1]
                
        # expand around center
        for i in range(len(s)):
            j = i
            k = i + 1
            
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            
            j += 1
            k -= 1
            if k - j + 1 > len(sol):
                sol = s[j:k+1]
                
        return sol
