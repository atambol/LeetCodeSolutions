class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import deque
        closing = "]})"
        opening = "[({"
        bracket = {
            "[": "]",
            "{": "}",
            "(": ")"
              }
        d = deque()
        for i in s:
            if i in opening:
                d.append(i)
            elif i in closing:
                try:
                    j = d.pop()
                    if i != bracket[j]:
                        return False
                except IndexError:
                    return False
        if len(d) > 0:
            return False
        else:
            return True
                
                
        
