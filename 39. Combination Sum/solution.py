class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # edge case
        if not candidates:
            return sol
        
        # sort the candidates
        candidates.sort()        
        return self.backtrack(candidates, target, 0)

        
    def backtrack(self, candidates, target, i):
        sol = []
        for j in range(i, len(candidates)):
            if target - candidates[j] == 0:
                sol.append([candidates[j]])
                break
            elif target - candidates[j] < 0:
                break
            else:
                sub = self.backtrack(candidates, target-candidates[j], j)
                for s in sub:
                    sol.append([candidates[j]] + s)
                
        return sol
