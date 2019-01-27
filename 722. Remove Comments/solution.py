class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        # final solution
        sol = []
        
        # flag for block level commenting
        blockComment = False
        
        # iterate over each line
        for line in source:
            l = len(line)
            i = 0
            
            # create a temp buffer to store valid characters
            if not blockComment:
                buffer = []
                
            while i < l:
                if blockComment:
                    # block comment ends here
                    if line[i] == "*" and i+1 < l and line[i+1] == "/":
                        i += 1
                        blockComment = False
                else:
                    if line[i] == "/" and i + 1 < l:
                        # block comment start
                        if line[i+1] == "*":
                            i += 1
                            blockComment = True
                        # in line comment starts
                        elif line[i+1] == '/':
                            break
                        # non-comment character - add to the buffer
                        else:
                            buffer.append(line[i])
                    # non-comment character
                    else:
                        buffer.append(line[i])
                i += 1
            
            # add only if the buffer is non empty and the block comment flag is not set
            if buffer and not blockComment:
                sol.append("".join(buffer))                
        return sol
