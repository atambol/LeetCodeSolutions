class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        
        count = [0]*26
        maxlen = 0
        i = 0
        j = 0
        while j < len(s):
            ind = ord(s[j]) - ord('A')
            count[ind] += 1
            j += 1
            while sum(count) - max(count) > k:
                ind = ord(s[i]) - ord('A')
                count[ind] -= 1
                i += 1
                
            maxlen = max(maxlen, j-i)

            
        return maxlen
