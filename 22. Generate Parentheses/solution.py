class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        if n == 0:
            return sol
        sol.append("()")
        if n == 1:
            return sol
        
        for i in range(1, n):
            newsol = set()
            for s in sol:
                for i in range(len(s)):
                    newsol.add(s[:i] + "()" + s[i:])
                    
            sol = newsol
            
        return list(sol)
