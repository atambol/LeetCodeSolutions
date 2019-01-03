class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s1 = []
        s2 = []
        
        # calculate the volume contained from left
        tallest = 0
        for h in height:
            if h > tallest:
                s1.append(0)
                tallest = h
            else:
                s1.append(tallest-h)
                
        # calculate the volume contained from right
        tallest  = 0
        for h in height[::-1]:
            if h > tallest:
                s2.append(0)
                tallest = h
            else:
                s2.append(tallest-h)
        s2.reverse()
        
        # calculate the total volume
        vol = 0
        for i, j in zip(s1, s2):
            vol += min(i, j)
            
        return vol
        
