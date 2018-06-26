map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Solution(object):        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        sol = []
        solution = Solution()
        if digits == "":
            return []
        if digits[1:] == "":
            return map[digits[0]]
        else:
            strings = solution.letterCombinations(digits[1:])
            for alpha in map[digits[0]]:
                # print alpha
                for string in strings:
                    sol.append(alpha + string)
            return sol
