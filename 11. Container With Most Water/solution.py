class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        
        n = len(height)
        area = 0
        i = 0
        j = n - 1
        
        while i < j:
            area = max((j-i)*min([height[i], height[j]]), area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
                
        return area
            
        
