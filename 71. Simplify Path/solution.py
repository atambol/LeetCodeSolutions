class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathSplit = path.split("/")
        stack = []
        for p in pathSplit:
            if not p or p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
                
        return "/" + "/".join(stack)
                
