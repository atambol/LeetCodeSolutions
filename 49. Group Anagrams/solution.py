class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in map:
                map[s_sorted].append(s)
            else:
                map[s_sorted] = [s]
        
        return [map[a] for a in map]
