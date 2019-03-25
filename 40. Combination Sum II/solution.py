class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        sol = []
        if not candidates:
            return sol
        candidates.sort()
        return self.backtrack(candidates, target, 0)
    
    def backtrack(self, candidates, target, start):
        sol = []

        for i in range(start, len(candidates)):
            diff = target - candidates[i]
            if diff < 0:
                break
            elif diff == 0:
                sol.append([candidates[i]])
                break
            else:
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                sub = self.backtrack(candidates, diff, i+1)
                for s in sub:
                    sol.append([candidates[i]] + s)
                    
        return sol
                
