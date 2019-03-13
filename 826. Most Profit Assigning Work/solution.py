class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], workers: List[int]) -> int:
        # combine
        tups = []
        for d, p in zip(difficulty, profit):
            tups.append([d, p])
            
        # sort by difficulty
        tups.sort(key=lambda x: (x[0], x[1]))
        
        # bubble up the max profit
        for i in range(1, len(tups)):
            tups[i][1] = max(tups[i-1][1], tups[i][1])

        # sort the workers
        workers.sort()
        
        # calculate the profits
        profit = 0
        while workers and tups:
            while tups and workers[-1] < tups[-1][0]:
                tups.pop()
                
            if tups:
                profit += tups[-1][1]
                
            workers.pop()
            
        return profit
