class Solution:
    def longestPalindrome(self, s: str) -> str:
        pali = ""
        for i in range(len(s)):
            for j in [i-1, i]:
                k = i + 1
                while j >= 0 and k < len(s) and s[j] == s[k]:
                    j -= 1
                    k += 1
                
                j += 1
                if len(pali) < k-j:
                    pali = s[j:k]
                    
        return pali
                
