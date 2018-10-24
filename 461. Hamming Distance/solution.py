class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        d = 0
        a = x ^ y
        while a:
            b = a >> 1
            b = b << 1
            
            if a != b:
                d += 1
                
            a = a >> 1
        
        return d
