class Solution:
    def removeKdigits(self, num: str, j: int) -> str:
        # edge case : remove all digits
        if j == len(num):
            return "0"
        
        # create a stack from the string
        stack = [int(n) for n in num]
        stack.reverse()
        aux = []
        
        # maintain an auxilary stack
        # check if the top of aux is greater than top of stack
        # basically check for the a decreasing order in the string
        while stack:
            if aux and j > 0 and stack[-1] < aux[-1]:
                aux.pop()
                j -= 1
            else:
                aux.append(stack.pop())
        
        # remove remaining j numbers from aux
        while j:
            aux.pop()
            j -= 1
        
        # check if all numbers left are 0s
        if aux.count(0) == len(aux):
            return "0"
        else:
            # remove any leading 0s
            i = 0
            while aux[i] == 0:
                i+= 1
            
            aux = aux[i:]
            
            # return the final string
            return "".join([str(n) for n in aux])
