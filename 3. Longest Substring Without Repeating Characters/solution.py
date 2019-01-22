class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        j = 0
        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                count = max(count, i - j)
                j = max(j, seen[s[i]] + 1)
            seen[s[i]] = i
            
        return max(count, len(s) - j)
