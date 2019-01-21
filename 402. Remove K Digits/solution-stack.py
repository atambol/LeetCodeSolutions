class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # edge cases
        if k >= len(num):
            return "0"
        
        # create a stack
        stack = []
        for digit in num[::-1]:
            stack.append(int(digit))

        # use an auxillary stack to store partial solution
        aux = []
        
        # remove elements until k is not 0 or stack runs out
        while k and stack: 
            if aux and stack[-1] < aux[-1]:
                k -= 1
                aux.pop()
            else:
                aux.append(stack.pop())
        
        # push back elements to stack
        while aux:
            stack.append(aux.pop())
        
        # remove any leading zeroes
        while stack and stack[-1] == 0:
            stack.pop()
            
        stack.reverse()
        
        # remove any remaining numbers 
        if k:
            stack = stack[:-k]
        
        # return the solution
        if stack:
            return "".join([str(e) for e in stack])
        else:
            return "0"
        
