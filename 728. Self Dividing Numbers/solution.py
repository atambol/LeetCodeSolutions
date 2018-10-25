class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sol = []
        for i in range(left, right+1):
            digits = self.getDigits(i)
            sdn = True
            for digit in digits:
                if digit == 0 or i % digit != 0:
                    sdn = False
                    break
                    
            if sdn:
                sol.append(i)
                
        return sol
    
    def getDigits(self, i):
        digits = set()
        for s in str(i):
            digits.add(int(s))
        return digits
