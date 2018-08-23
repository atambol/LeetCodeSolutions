class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        strings = []
        count = 0
        for s in S[::-1]:
            if s == "-":
                continue
            if count and count % K == 0:
                strings.append("-")
            asci = ord(s)
            if asci >= 97:
                strings.append(chr(asci - 32))
            else:
                strings.append(s)
                
            count+=1

        return "".join(strings[::-1])
                
