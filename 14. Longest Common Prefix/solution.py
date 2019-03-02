class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge case
        if not strs:
            return ""
        
        # extract the first string
        stack = []
        for s in strs[0]:
            for t in s:
                stack.append(t)
            
        # check other strings
        for s in strs[1:]:
            i = 0
            for t in s:
                if i < len(stack) and t != stack[i]:
                    break
                    
                i += 1
            
            while len(stack) > i:
                stack.pop()
                
        return "".join(stack)
