class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Edge case
        if n == 0:
            return []
        else:
            # for i = 0
            sol = ["()"]
            
            # for i = 1 .. n-1
            for i in range(1, n):
                tmp = set()
                # for every combination found until now
                for s in sol:
                    # for every point between adjacent characters in the combination
                    for j in range(len(s)):
                        # insert a paranthesis
                        tmp.add(s[:j] + "()" + s[j:])
                        
                # Take care of repetitions due to symmetrical strings
                sol = list(tmp)
                
            return sol
        
            
