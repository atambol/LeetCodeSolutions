class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge cases
        n = len(s)
        if n < 2:
            return n
        
        # run two pointer i and j
        i = 0
        maxLen = 0
        
        # maintain a map of character to indices
        map = {}
        
        for j in range(n):
            if s[j] in map:
                i = max(map[s[j]] + 1, i) ## this step is important
            map[s[j]] = j
            maxLen = max(maxLen, j-i+1)
            
        return maxLen
                
                
                
