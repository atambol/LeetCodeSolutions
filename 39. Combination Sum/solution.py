class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # edge case
        if not candidates and not target:
            return []
        
        # backtrack over each target
        candidates.sort()
        return self.backtrack(candidates, target, 0)
        
    def backtrack(self, candidates, target, index):
        sol = []
        for i, c in enumerate(candidates[index:]):
            if target == c:
                sol.append([c])
            elif target > c:
                subsol = self.backtrack(candidates, target-c, i+index)
                for s in subsol:
                    sol.append([c]+s)
            else:
                break
                
        return sol
