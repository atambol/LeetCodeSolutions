class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #### Sieve of Eratosthenes
        # edge cases
        if n == 0 or n == 1:
            return 0
        
        # create a list to store prime test result of ith number
        primes = [True]*(n)
        primes[0] = False
        primes[1] = False
        
        # loop from 2 to n-1 to find primes
        for i in range(2,n-1):
            if primes[i]:
                # remove all the numbers that are a multiple
                j = i+i
                while j < n:
                    primes[j] = False
                    j = j+i
        
        # count the primes
        return primes.count(True)
        
