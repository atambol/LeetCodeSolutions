class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # edge case
        if not candidates or not target:
            return []
        
        # backtrack
        candidates.sort()
        return self.backtrack(candidates, target, 0)
        
    def backtrack(self, candidates, target, index):
        sol = []
        
        # range over each candidate starting from index
        for i in range(index, len(candidates)):
            c = candidates[i]
            
            # terminal case - failure
            if target < c:
                return sol
            
            # terminal case - success
            elif target == c:
                sol.append([c])
                return sol
            
            else:
                # prevent repeated solutions
                if i != index and c == candidates[i-1]:
                    continue
                    
                # keep searching
                for s in self.backtrack(candidates, target-c, i+1):
                    sol.append([c]+s)
            
        return sol
            
