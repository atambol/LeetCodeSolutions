class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        ncol = len(matrix[0])
        i = len(matrix)-1
        j = 0
        
        while i >= 0 and j < ncol:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j+=1
            else:
                i-=1
                
        return False
        
