class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        
        # dont need to check if distance is more than 1
        if abs(n - m) > 1:
            return False
        
        # if string are same then no point
        if s == t:
            return False
        
        # edge case - if there is just one character
        if n + m == 1:
            return True
        
        # two pointer
        edited = False
        i = 0
        j = 0
        
        while i < n and j < m:
            # increment both ptrs until string is same
            if s[i] == t[j]:
                i += 1
                j += 1
                
            else:
                # if the string is edited once, then it cannot be edited twice
                if edited:
                    return False
                
                # mark edited
                edited = True
                
                # update pointers
                if n == m:
                    i += 1
                    j += 1
                elif n > m:
                    i += 1
                else:
                    j += 1
                        
        return True
