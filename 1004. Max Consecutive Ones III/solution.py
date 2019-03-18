class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count = 0
        
        # edge case
        if not A:
            return count
        
        i = 0
        j = 0
        k = 0
        while j < len(A):
            if A[j] == 0:
                k += 1
            
            while k > K and i <= j:
                if A[i] == 0:
                    k -= 1
                i += 1
            
            count = max(count, j-i+1)
            j += 1
        
        return count
