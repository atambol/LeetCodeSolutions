class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0]*26
        for t in s:
            i = ord(t) - ord('a')
            count[i] += 1
            
        for j, t in enumerate(s):
            i = ord(t) - ord('a')
            if count[i] == 1:
                return j
            
        return -1
            
