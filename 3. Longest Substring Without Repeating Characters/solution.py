class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = ""
        prevsol = ''
        for x in s:
            if x not in sol:
                sol += x
            else:
                if len(sol) > len(prevsol):
                    prevsol = sol
                index_of_repeat = sol.index(x)
                sol = sol[index_of_repeat+1:] + x
        return max(len(prevsol), len(sol))
