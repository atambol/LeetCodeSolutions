class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0]*26
        i = 0 
        j = 0
        maxLen = 0
        
        # Sliding window
        while j < len(s):
            # insert letter count
            index = ord(s[j]) - ord("A")
            counts[index] += 1
            j += 1

            # update counts array so as to have max k updates
            while sum(counts) - max(counts) > k:
                index = ord(s[i]) - ord("A")
                counts[index] -= 1
                i += 1
    
            maxLen = max(maxLen, sum(counts))
            
            
        return maxLen
