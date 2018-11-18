class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # edge cases
        if not cost:
            return 0
        if len(cost) <= 2:
            return min(cost)
        
        # init
        total = []
        for c in cost:
            total.append(c)
        
        # DP
        for i in range(2, len(cost)):
            total[i] += min(total[i-1], total[i-2])
            
        return min(total[-1], total[-2])
            
