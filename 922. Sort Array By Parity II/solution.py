class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        
        while i < j:
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
                
            elif A[i] % 2 == 1:
                j -= 1
            
            elif A[j] % 2 == 0:
                i += 1
                
            else:
                i += 1
                j -= 1
                
        i = 1
        j = len(A) - 2
        
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 2
            j -= 2
            
        return A
