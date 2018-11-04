class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        longestSubstringLength = -1
        seen = {}
        while i < len(s):
            if s[i] in seen:
                if len(seen.keys()) > longestSubstringLength:
                    longestSubstringLength = len(seen.keys())
                    
                i = seen[s[i]] + 1
                seen = {}
            else:
                seen[s[i]] = i
                i += 1
        
        if len(seen.keys()) > longestSubstringLength:
            longestSubstringLength = len(seen.keys())
            
        return longestSubstringLength
