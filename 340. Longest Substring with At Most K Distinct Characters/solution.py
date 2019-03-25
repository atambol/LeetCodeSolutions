class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        unique = {}
        l = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in unique:
                unique[s[j]] = 0
            unique[s[j]] += 1
            j += 1
            
            while len(unique) > k:
                unique[s[i]] -= 1
                if unique[s[i]] == 0:
                    unique.pop(s[i])
                    
                i += 1
                
            l = max(l, j - i)
            
        return l
                    
