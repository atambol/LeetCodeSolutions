from collections import defaultdict
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        map = defaultdict(lambda: [])
        
        for i in range(len(B)):
            map[B[i]].append(i)
            
        res = []
        for i in range(len(A)):
            res.append(map[A[i]][-1])
            map[A[i]] = map[A[i]][:-1]
        
        return res
