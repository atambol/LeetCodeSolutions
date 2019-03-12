class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # edge case
        if not candidates or not target:
            return []
        
        # sort and backtrack
        candidates.sort()
        return self.backtrack(candidates, target, 0)
        
    def backtrack(self, candidates, target, n):
        sol = []
        for i in range(n, len(candidates)):
            if target - candidates[i] == 0:
                sol.append([candidates[i]])
                break
            elif target > candidates[i]:
                if i != n and candidates[i-1] == candidates[i]:
                    continue
                    
                sub = self.backtrack(candidates, target-candidates[i], i+1)
                for s in sub:
                    sol.append([candidates[i]] + s)
            else:
                break
                
        return sol
