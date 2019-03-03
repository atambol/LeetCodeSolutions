class Solution:
    def simplifyPath(self, path: str) -> str:
        if not str:
            return ""
        
        stack = []
        paths = path.split("/")
        for p in paths:
            if not p or p == '.':
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
                
        s = "/".join(stack)
        return "/"+s
            
