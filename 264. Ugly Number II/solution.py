import heapq

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # use three pointers to track indices corresponding to 2, 3 and 5
        n1 = 0
        n2 = 0
        n3 = 0
        
        # maintain the ugly array
        uglies = [1]
        
        while n > 1:
            # get the smallest ugly number
            ugly = min(uglies[n1]*2, uglies[n2]*3, uglies[n3]*5)
            
            # update the pointers
            if ugly == uglies[n1]*2:
                n1 += 1
            elif ugly == uglies[n2]*3:
                n2 += 1
            elif ugly == uglies[n3]*5:
                n3 += 1
            
            # append it only if not a duplicate
            if ugly != uglies[-1]:
                uglies.append(ugly)
                n -= 1

        return uglies[-1]
                
