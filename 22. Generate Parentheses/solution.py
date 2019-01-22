class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        sol = set()
        
        # edge case
        if not n:
            return []
        
        # base case
        sol.add("()")
        
        # generate 
        for i in range(1, n):
            newsol = set()
            # for every combination previously seen
            for s in sol:
                for i in range(len(s)):
                    newsol.add(s[:i] + "()" + s[i:])
                    
            sol = newsol
            
        return list(sol)
