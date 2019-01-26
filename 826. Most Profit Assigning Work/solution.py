class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # edge cases
        if not profit:
            return 0
        
        if not worker:
            return 0
        
        # create a list of list
        tup = [[d, p] for d, p in zip(difficulty, profit)]
        
        # sort by difficulty
        tup.sort(key=lambda x: (x[0], x[1]))
        
        # propagate the maximum profit
        for i in range(1, len(tup)):
            tup[i][1] = max(tup[i][1], tup[i-1][1])
            
        # sort the workers
        worker.sort()
        
        # calculate the profit
        profit = 0
        while worker:
            while tup and worker[-1] < tup[-1][0]:
                tup.pop()
                
            if tup:
                profit += tup[-1][1]
            worker.pop()
                
        return profit
