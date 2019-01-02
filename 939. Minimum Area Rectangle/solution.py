class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        mapx = {}

        for point in points:
            x = point[0]
            y = point[1]
            try:
                mapx[x].append(y)
            except:
                mapx[x] = [y]
        
        seen = {}
        minArea = sys.maxsize
        Xs = sorted(list(mapx))
        for i, x1 in enumerate(Xs):
            mapx[x1].sort()
            for j, y1 in enumerate(mapx[x1]):
                for k, y2 in enumerate(mapx[x1][j+1:]):
                    if (y1, y2) in seen:
                        x2 = seen[(y1, y2)]
                        minArea = min(minArea, abs((x2-x1)*(y2-y1)))
                    seen[(y1, y2)] = x1
                    
        if sys.maxsize == minArea:
            return 0
        else:
            return minArea
            
