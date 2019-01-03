class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # edge cases
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        if not n:
            return False
        
        # start from bottom left
        i = m-1
        j = 0
        
        # check for target in O(m+n)
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
                
        return False
