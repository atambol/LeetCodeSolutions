class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # O(n) solution
        i = 0
        j = len(height) - 1
        maxArea = 0
        
        # keep moving i and j closer while keeping the larger height
        while i < j:
            area = min(height[i], height[j])*(j-i)
            if area > maxArea:
                maxArea = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea
