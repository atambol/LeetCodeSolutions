class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # edge case
        if len(height) < 2:
            return 0
        
        # two pointer
        i = 0
        j = len(height) - 1
        vol = 0
        
        while i < j:
            vol = max(vol, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return vol
