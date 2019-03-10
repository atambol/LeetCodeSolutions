class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        maxlen = 0
        
        i = 0
        j = 0
        seen = {}
        while j < len(s):
            maxlen = max(maxlen, j-i)
            if s[j] in seen:
                i = max(i, seen[s[j]]+1)
            
            seen[s[j]] = j
            
            j += 1
            
        return max(maxlen, j-i)
