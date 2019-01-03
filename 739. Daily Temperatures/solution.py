class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        index = {}
        sol = []
        
        # use a stack to keep track of previous temperatures
        # use a dictionary to keep track of the index of prev temperatures
        for i in range(len(T)-1, -1, -1):
            t = T[i]
            while stack and stack[-1] <= t:
                stack.pop()
                
            if not stack:
                sol.append(0)
            else:
                sol.append(index[stack[-1]] - i)
                
            index[t] = i
            stack.append(t)
        
        return sol[::-1]
