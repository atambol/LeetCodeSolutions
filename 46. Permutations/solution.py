class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        # edge case
        if not nums:
            return sol
        
        numset = set(nums)
        
        # backtrack
        return self.backtrack(numset)
        
    # O(n!) for backtracking over numset of size n
    def backtrack(self, numset):    
        sol = []
        
        # base case
        if len(numset) == 1:
            num = numset.pop()
            sol.append([num])
            numset.add(num)
        else:
            # loop over n numbers
            nums = list(numset)
            for num in nums:
                numset.remove(num)
                sub = self.backtrack(numset)
                for s in sub:
                    s.append(num)
                    sol.append(s)
                numset.add(num)
        return sol
            
