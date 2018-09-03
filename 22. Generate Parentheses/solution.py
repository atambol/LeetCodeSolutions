class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtracker(string = "", left = 0, right = 0):
            if len(string) == 2*n:
                res.append(string)
                return
            if left < n:
                backtracker(string+"(", left+1, right)
            if right < left:
                backtracker(string+")", left, right+1)
        backtracker()
        return res
