class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        sol = []
        for i in range(len(T)-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()

            if stack:
                sol.append(stack[-1] - i)
            else:
                sol.append(0)
                
            stack.append(i)
        sol.reverse()
        return sol
                
        
