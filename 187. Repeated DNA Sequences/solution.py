class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        seq = {}
        sol = []
        for i in range(len(s)):
            try:
                seq[s[i:i+10]] += 1
                if seq[s[i:i+10]] == 2:
                    sol.append(s[i:i+10])
            except:
                seq[s[i:i+10]] = 1
                
        return sol
