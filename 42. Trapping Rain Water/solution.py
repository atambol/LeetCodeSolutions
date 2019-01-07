class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # edge case
        if len(height) <= 2:
            return 0
        
        # calculate from the left 
        maxHeight = height[0]
        right = [0]
        for h in height[1:]:
            if maxHeight > h:
                right.append(maxHeight - h)
            else:
                right.append(0)
                maxHeight = h

        # calculate from the right
        height.reverse()
        maxHeight = height[0]
        left = [0]
        for h in height[1:]:
            if maxHeight > h:
                left.append(maxHeight - h)
            else:
                left.append(0)
                maxHeight = h
                
        left.reverse()
        
        # calculate the vol
        vol = 0
        for l, r in zip(left, right):
            vol += min(l, r)
        print(left, right)
        return vol
                
