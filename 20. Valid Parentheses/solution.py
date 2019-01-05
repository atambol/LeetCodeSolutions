class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {
            "{":"}",
            "(":")",
            "[":"]"
        }

        for t in s:
            if t in map:
                stack.append(t)
            else:
                if not stack:
                    return False
                else:
                    para = stack.pop()
                    if map[para] != t:
                        return False
                    
        return not stack
