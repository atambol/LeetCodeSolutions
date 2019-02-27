class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x:(x[0], x[1]))
        count = 0
        
        end = points[0][1]
        for x, y in points[1:]:
            if x > end:
                count += 1
                end = y
            else:
                end = min(end, y)
                
        return count+1
