class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sol = {}
        
        for s in strs:        
            key = "".join(sorted(s))
            if key in sol:
                sol[key].append(s)
            else:
                sol[key] = [s]
            
        return list(sol.values())
            
