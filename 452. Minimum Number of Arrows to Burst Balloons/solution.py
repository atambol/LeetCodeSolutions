class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # edge case
        if not points:
            return 0
        
        # sort points
        points.sort(key = lambda x: (x[0], x[1]))
        
        # traverse all the points
        count = 0
        limit = sys.maxsize
        for i in range(len(points)):
            if points[i][0] > limit:
                count += 1
                limit = points[i][1]
            else:
                limit = min(limit, points[i][1])
                
        return count+1
