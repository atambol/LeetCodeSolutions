class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # edge case
        if not n:
            return []
        
        sol = set(["()"])
        if n == 1:
            return list(sol)
        
        for i in range(n-1):
            newsol = set()
            for s in sol:
                for j in range(len(s)):
                    newsol.add(s[:j] + "()" + s[j:])
                    
            sol = newsol
            
        return list(sol)
