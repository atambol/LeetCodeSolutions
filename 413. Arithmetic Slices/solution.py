class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # edge cases - the slice needs to be of atleast size 3
        if len(A) < 3:
            return 0
        
        sol = 0
        
        # get the difference betweeen first two elements
        diff = A[1] - A[0]
        start = 0
        
        # increment end until the difference stays the same
        for end in range(2, len(A)):
            # if the difference changes, calculate the possible number of slices and update end and start
            if diff != A[end] - A[end-1]:
                sol += self.countSlices(len(A[start:end]))
                start = end - 1
                diff = A[end] - A[end-1]
            end += 1
            
        # calculate the number of possible slices from the last 
        if start != end:
            sol += self.countSlices(len(A[start:]))
            
        return sol
                
        
    def countSlices(self, n):
        if n < 3:
            return 0
        elif n == 3:
            return 1
        else:
            n = n-2
            return int(n*(n+1)/2)
