class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        sol = []
        for v in version1.split("."):
            sol.append(int(v))
        version1 = sol
        
        sol = []    
        for v in version2.split("."):
            sol.append(int(v))
        version2 = sol
        
        m = len(version1)
        n = len(version2)
        
        if m > n:
            version2.extend([0] * (m-n))
        elif n > m:
            version1.extend([0] * (n-m))
        
        l = max(m, n)
        for i in range(l):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1

        return 0
