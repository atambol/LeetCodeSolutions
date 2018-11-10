class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # handle edge cases
        if n == 0:
            return 1
        if n == 1:
            return x
        
        # handle negative powers
        if n < 0:
            x = 1/x
            n = abs(n)
            
        # get the power split
        powers = self.getPowerSplit(n)
        maxPower = max(powers)
        
        # Calculate the powers of x upto the max power in powers (dynamic programming)
        p = 1
        num = x
        map = {}
        while p <= maxPower:
            map[p] = num
            p *= 2
            num *= num
            
        # Multiply all the necessary powers to get x^n
        sol = 1
        for power in powers:
            sol *= map[power]
            
        return sol
        
    # get the power split of n in terms of multiple of 2, for eg: if n = 10, powers = [8,2]
    def getPowerSplit(self, n):
        powers = []
        while n > 0:
            p = 1
            while p*2 <= n:
                p *= 2
            
            powers.append(p)
            n = n - p
        return powers
            
