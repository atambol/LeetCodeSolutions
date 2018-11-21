class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
            
        diff = len(version1) - len(version2)
        if diff < 0:
            version1.extend(["0"]*abs(diff))
        elif diff > 0:
            version2.extend(["0"]*diff)
        
        result = 0
        print(version1, version2)
        for i in range(len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
        
        return result
