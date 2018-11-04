class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for i in range(len(s)):
            if s[i] in "{([":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if map[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
