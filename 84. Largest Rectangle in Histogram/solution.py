class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ## O(n) solution
        # edge case 
        area = 0
        n = len(heights)
        if not n:
            return area
        
        # look left
        left = [1]*n
        for i in range(1, n):
            j = i - 1
            while j >= 0 and heights[i] <= heights[j]:
                left[i] += left[j]
                j -= left[j]
                
        # look right
        right = [1]*n
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and heights[i] <= heights[j]:
                right[i] += right[j]
                j += right[j]
                
        # calculate area
        for i in range(n):
            area = max(area, heights[i]*(left[i] + right[i] - 1))
            
        return area
