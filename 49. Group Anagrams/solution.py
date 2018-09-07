from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        memory = defaultdict(lambda: [])
        for s in strs:
            memory["".join(sorted(s))].append(s)
            
        res = []
        for key in memory.keys():
            res.append(memory[key])
                
        return res
