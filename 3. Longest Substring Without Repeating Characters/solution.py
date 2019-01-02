class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case
        if not s:
            return 0
        
        # pointers initialized
        i = 0
        j = 0
        seen = {}
        maxLen = 0
        
        # loop over each char
        for j, char in enumerate(s):
            if char in seen:
                # move the first pointer to the max position - either after the repeating char or the new i
                i = max(seen[char] + 1, i)
            seen[char] = j
            maxLen = max(maxLen, j-i+1)
        return maxLen
