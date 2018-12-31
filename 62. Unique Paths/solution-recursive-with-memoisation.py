from collections import defaultdict

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            return 1
        else:
            memo = []
            for i in range(m):
                memo.append([0]*n)
            self.getPathCount(memo, 0, 0, m-1, n-1)
            return memo[0][0]
        
    def getPathCount(self, memo, x, y, m, n):
        if x > m or y > n:
            return 0
        elif x == m and y == n:
            return  1
        else:
            if not memo[x][y]:
                # print(x,y)
                memo[x][y] = self.getPathCount(memo, x + 1, y, m, n) + self.getPathCount(memo, x, y + 1, m, n)
            return memo[x][y]
