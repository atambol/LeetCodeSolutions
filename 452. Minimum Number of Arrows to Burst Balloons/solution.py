class Solution:
    def findMinArrowShots(self, points: 'List[List[int]]') -> 'int':
        # edge case
        if not points:
            return 0
        
        # this problem is similar to meeting rooms 2
        arrows = 0
        n = len(points)
        points.sort(key=lambda x: (x[0], x[1]))
        
        # greedy approach
        i = 0
        while i < n:
            y = points[i][1]
            j = i + 1
            while j < n and points[j][0] <= y:
                y = min(y, points[j][1]) # all points seen so far should have a common edge
                j += 1
            arrows += 1
            i = j
            
        return arrows
