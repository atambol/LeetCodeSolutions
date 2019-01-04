class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # create a map from x values to list of y values
        cols = {}
        for x,y in points:
            try:
                cols[x].append(y)
            except KeyError:
                cols[x] = [y]
                
        minArea = sys.maxsize
        seen = {}
        X = sorted(list(cols))
        for x in X:
            cols[x].sort()
            y = cols[x]
            for i in range(len(y)):
                for j in range(i+1, len(y)):
                    # look for previously seen pairs of y and calculate area
                    if (y[i], y[j]) in seen:
                        area = (x - seen[(y[i], y[j])])*(y[j] - y[i])
                        minArea = min(area, minArea)
                    seen[(y[i], y[j])] = x
                    
        if minArea == sys.maxsize:
            return 0
        return minArea
                    
        
