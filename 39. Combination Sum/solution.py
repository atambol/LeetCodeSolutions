class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        if not candidates:
            return sol
        
        candidates.sort()
        sol = self.backtrack(candidates, target, 0)
        for s in sol:
            s.reverse()
            
        return sol
        
    def backtrack(self, candidates, target, n):
        sol = []
        for i in range(n, len(candidates)):
            sub = []
            if target - candidates[i] < 0:
                break
            elif target - candidates[i] == 0:
                sub.append([candidates[i]])
            else:
                sub = self.backtrack(candidates, target-candidates[i], i)
                for s in sub:
                    s.append(candidates[i])
            if sub:
                sol.extend(sub)
                
        return sol
            
