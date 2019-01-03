class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # edge case
        if len(s) < 2:
            return s
        
        n = len(s)
        # expand around an index
        maxStr = ""
        for i in range(n):
            k = i - 1
            j = i + 1
            
            # keep expanding until fault
            while k >= 0 and j < n and s[k] == s[j]:
                j += 1
                k -= 1
            
            # recover
            k += 1
            j -= 1
            
            # calculate the expansion
            if j-k+1 > len(maxStr):
                maxStr = s[k:j+1]
                
        # expand between indices
        for i in range(n-1):
            k = i
            j = i + 1
            
            # keep expanding until fault
            while k >= 0 and j < n and s[k] == s[j]:
                j += 1
                k -= 1
            
            # recover
            k += 1
            j -= 1
            
            # calculate the expansion
            if j-k+1 > len(maxStr):
                maxStr = s[k:j+1]
                
        return maxStr
