class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seen = {}
        map = {}
        for x, y in points:
            try:
                map[x].add(y)
            except:
                map[x] = set([y])
                
        minSize = sys.maxsize
        X = sorted(list(map))
        for x in X:
            Y = sorted(list(map[x]))
            for i in range(len(Y)):
                for j in range(i+1, len(Y)):
                    if (Y[i], Y[j]) in seen:
                        x2 = seen[(Y[i], Y[j])]
                        minSize = min(minSize, abs((x2-x)*(Y[i]-Y[j])))
                    seen[(Y[i], Y[j])] = x
        if minSize == sys.maxsize:
            return 0
        return minSize
