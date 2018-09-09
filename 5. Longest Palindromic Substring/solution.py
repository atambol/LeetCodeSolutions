class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        pali = []*l
     
        start = 0
        end = 0
        
        for i in range(l):
            pali.append([])
            for j in range(l):
                    pali[i].append(i==j)
            
        for i in range(1, l):
            if s[i] == s[i-1]:
                pali[i-1][i] = True
                start = i-1
                end = i
            else:
                pali[i-1][i] = False
        
        if l >= 3:
            base = 0
            diff = 2 

            while diff < l:
                i = base
                j = base + diff
                while j < l:
                    if pali[i+1][j-1] and s[i] == s[j]:
                        pali[i][j] = True
                        start = i
                        end = j
                    else:
                        pali[i][j] = False
                    i += 1
                    j += 1
                diff += 1

        # for i in range(l):
        #     print(pali[i])
        return s[start:end+1]
        
