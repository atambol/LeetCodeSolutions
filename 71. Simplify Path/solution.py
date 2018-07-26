class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        vars = path.split("/")
        useless_operations = ["", "."]
        solution = []
        for var in vars:
            if var not in useless_operations:
                if var == '..':
                    try:
                        solution.pop()
                    except IndexError:
                        continue
                else:
                    solution.append(var)
                    
        return "/" + "/".join(solution)
