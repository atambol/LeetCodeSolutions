class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        sol = []
        if n == 0:
            return sol
        
        sol.append("()")
        if n == 1:
            return sol
        
        # sol should be a set to disallow any repeated sequences
        sol = set(sol)
        
        # loop n-1 times more
        for i in range(1, n):
            
            # construct new solutions by using existing solutions
            newsol = set()
            for s in sol:
                
                # pick every single string, and insert parenthesis around every index in it
                for j in range(n):
                    newsol.add(s[:j] + "()" + s[j:])
                    
            sol = newsol
            
        # return a list
        return list(sol)
