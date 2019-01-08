class Solution:
    def __init__(self):
        self.memo = {}
        
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = 0
        col = 0
        if not triangle or not triangle[0]:
            return 0
        
        return self.recur(row, col, triangle)
        
    def recur(self, row, col, triangle):
        if row < len(triangle):
            if (row+1, col) in self.memo:
                left = self.memo[(row+1, col)]
            else:
                left = self.recur(row+1, col, triangle)
                
            if (row+1, col+1) in self.memo:
                right = self.memo[(row+1, col)]
            else:   
                right = self.recur(row+1, col+1, triangle)
            
            sol = min(left, right) + triangle[row][col]
            self.memo[(row, col)] = sol
            return sol
        else:
            return 0
