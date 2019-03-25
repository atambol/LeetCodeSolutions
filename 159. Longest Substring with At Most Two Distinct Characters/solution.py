class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique = {}
        i = 0
        j = 0
        l = 0
        while j < len(s):
            if s[j] not in unique:
                unique[s[j]] = 0
            unique[s[j]] += 1
            j += 1
            if len(unique) > 2:
                unique[s[i]] -= 1
                if not unique[s[i]]:
                    unique.pop(s[i])
                    
                i += 1
                
            l = max(l, j-i)
            
        return l
