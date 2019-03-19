class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        
        distinct = {}
        l, r = 0, 0
        count = 0
        while r < len(s):
            if s[r] not in distinct:
                distinct[s[r]] = 0
            distinct[s[r]] += 1
                     
            r += 1
            
            while len(distinct) > 2:
                distinct[s[l]] -= 1
                if not distinct[s[l]]:
                    distinct.pop(s[l])
                l += 1
                    
            count = max(count, r - l)
            
        return count
