class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case
        if len(height) < 3:
            return 0
        
        # get water stored above a column by looking left only
        left = [0]
        maxh = height[0]
        for h in height[1:]:
            if h < maxh:
                left.append(maxh - h)
            else:
                maxh = h
                left.append(0)
            
        # get water stored above a column by looking right only
        right = [0]
        maxh = height[-1]
        # height.reverse()
        for h in height[-2::-1]:
            if h < maxh:
                right.append(maxh - h)
            else:
                maxh = h
                right.append(0)
        right.reverse()
        
        # minimize the water content based on left and right view
        vol = 0
        for l, r in zip(left, right):
            vol += min(l, r)
            
        return vol
                
        
