class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        minA = min(A)
        maxA = max(A)
        
        if minA + 2*K < maxA:
            return maxA - minA - 2*K
        else:
            return 0
