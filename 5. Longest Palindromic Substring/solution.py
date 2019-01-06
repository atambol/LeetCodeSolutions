class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # edge cases
        n = len(s)
        if n <= 1:
            return s
        
        maxLen = 0
        sol = ""
        # grow around an index
        for i in range(n):
            j = i - 1
            k = i + 1
            while k < n and j >= 0 and s[k] == s[j]:
                k += 1
                j -= 1
            if k - j - 1 > maxLen:
                sol = s[j+1:k]
            maxLen = max(maxLen, k-j-1)
            
        # grow between an index
        for i in range(n-1):
            j = i
            k = i + 1
            while k < n and j >= 0 and s[k] == s[j]:
                k += 1
                j -= 1
            if k - j - 1 > maxLen:
                sol = s[j+1:k]
            maxLen = max(maxLen, k-j-1)
            
        return sol
