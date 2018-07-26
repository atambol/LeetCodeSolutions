class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        permutations = self.getPermutations(s)
        validIPs = []
        for p in permutations:
            validIP = True
            for n in p:
                if int(n) > 255:
                    validIP = False
                    break
            if validIP:
                validIPs.append(".".join(p))
        return validIPs

    def getPermutations(self, s):
        permutations = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if i+j+k >= len(s):
                        continue
                    p = [s[:i], s[i:i+j], s[i+j:i+j+k], s[i+j+k:]]
                    skip = False
                    for n in p:
                        if n.startswith("0") and not n == "0":
                            skip = True
                            break
                    if not skip:
                        permutations.append(p)
        # print(permutations)
        return permutations
                
        
