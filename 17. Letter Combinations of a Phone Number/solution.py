class Solution:
    def __init__(self):
        self.map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        if len(digits) == 1:
            return self.map[digits[0]]
        
        combination = self.map[digits[0]]
        child_combination = self.letterCombinations(digits[1:])
        sol = []
        for i in combination:
            for j in child_combination:
                sol.append(i+j)
                
        return sol
