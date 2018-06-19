class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        # if i < 1:
        #     return 0
        
        count = 0
        while not i < 0:
            if s[i] == ' ':
                if count > 0:
                    return count
            else:
                count += 1
            i-=1
        return count
        
