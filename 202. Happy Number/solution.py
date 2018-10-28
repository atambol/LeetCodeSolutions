class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fptr = n
        sptr = n

        # Floyd cycle detection algorithm
        while True:
            fptr = self.sqDigits(self.sqDigits(fptr))
            sptr = self.sqDigits(sptr)
            print(sptr)
            if sptr == 1:
                return True
            if fptr == sptr:
                return False

    def sqDigits(self, n):
        digits = []
        while n:
            digits.append(n%10)
            n = n // 10
            
        total = 0
        for digit in digits:
            total += digit*digit
        
        return total
            
