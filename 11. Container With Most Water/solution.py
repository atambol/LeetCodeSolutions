class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # edge cases
        n = len(height)
        maxArea = 0
        if n < 2:
            return maxArea
        
        # two pointer technique
        i = 0
        j = n - 1
        while i < j:
            area = min(height[i], height[j])*(j-i)
            if area > maxArea:
                maxArea = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
                
        return maxArea
                
