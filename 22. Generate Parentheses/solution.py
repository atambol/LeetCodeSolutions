class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        else:
            sol = ["()"]
            for i in range(1, n):
                tmp = set()
                for s in sol:
                    for j in range(len(s)):
                        tmp.add(s[:j] + "()" + s[j:])
                sol = list(tmp)
                
            return sol
        
            
