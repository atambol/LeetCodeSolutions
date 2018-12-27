class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = []
        for i in range(2, n):
            isPrime = True
            for prime in primes:
                if prime*prime > i:
                    break
                if i % prime == 0:
                    isPrime = False
                    break
                    
            if isPrime:
                primes.append(i)
                
        return len(primes)
