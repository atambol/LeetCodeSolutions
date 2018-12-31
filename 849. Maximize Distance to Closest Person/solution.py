class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxD = 0
        vacant = 0
        found = False
        for seat in seats:
            if seat == 1:
                if not found:
                    maxD = max(maxD, vacant)
                    found = True
                else:
                    if vacant%2 == 0:
                        maxD = max(maxD, vacant//2)
                    else:
                        maxD = max(maxD, (vacant+1)//2)
                vacant = 0
            else:
                vacant += 1
        maxD = max(maxD, vacant)
            
        return maxD
