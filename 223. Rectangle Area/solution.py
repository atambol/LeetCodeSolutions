class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        r1 = [A, B, C, D]
        r2 = [E, F, G, H]
        r3 = self.getOverlap(r1, r2)
        area1 = self.getArea(r1)
        area2 = self.getArea(r2)
        if r3:
            area3 = self.getArea(r3)
        else:
            area3 = 0
            
        return area1 + area2 - area3
        
    def getArea(self, r):
        return abs(r[0]-r[2])*abs(r[1]-r[3])
    
    def getOverlap(self, r1, r2):
        # separate and mark x and y coordinates for both rectangles
        x = [(r1[0], "r1"), (r1[2], "r1"), (r2[0], "r2"), (r2[2], "r2")]
        y = [(r1[1], "r1"), (r1[3], "r1"), (r2[1], "r2"), (r2[3], "r2")]
        
        # sort them
        x.sort(key=lambda z: z[0])
        y.sort(key=lambda z: z[0])
        
        # if the markers dont alternate for either x or y, no overlap occurs
        if x[0][1] == x[1][1] or y[0][1] == y[1][1]:
            return []
        else:
            return [x[1][0], y[1][0], x[2][0], y[2][0]]
