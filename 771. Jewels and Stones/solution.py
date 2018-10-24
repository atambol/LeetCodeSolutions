from collections import defaultdict

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        stones = defaultdict(int)
        for s in S:
            stones[s] += 1
        
        res = 0
        for j in J:
            res += stones[j]
            
        return res
