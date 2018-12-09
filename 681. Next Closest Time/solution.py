class Solution(object):
    def __init__(self):
        self.map = None
        
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        self.map = self.getMap(time)
        digits = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]
        digits = self.getNext(digits)
        while not self.isValid(digits):
            print(digits)
            digits = self.getNext(digits)
            
        return "{}{}:{}{}".format(digits[0], digits[1], digits[2], digits[3])
        
    # get the cyclic clock for the given digits
    def getMap(self, time):
        time = set([int(time[0]), int(time[1]), int(time[3]), int(time[4])])
        digits = sorted(list(time))
        map = {}
        l = len(digits)
        for i, digit in enumerate(digits):
            map[digit] = digits[(i+1)%l]
            
        return map
    
    # check for time to be valid
    def isValid(self, digits):
        hours = digits[0]*10 + digits[1]
        minutes = digits[2]*10 + digits[3]
        return hours < 24 and minutes < 60
    
    # get the next time
    def getNext(self, digits):
        newDigits = []
        carry = True
        for digit in digits[::-1]:
            if carry:
                newDigits.append(self.map[digit])
                if self.map[digit] > digit:
                    carry = False
            else:
                newDigits.append(digit)
                
        return newDigits[::-1]
