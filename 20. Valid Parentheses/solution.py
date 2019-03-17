class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        
        for t in s:
            if t in map:
                stack.append(t)
            else:
                if not stack:
                    return False
                o = stack.pop()
                if map[o] != t:
                    return False
                
        if stack:
            return False
        
        return True
