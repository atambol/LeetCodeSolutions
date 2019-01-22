class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        sol = []
        stack = []
        for i in range(len(T)-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            
            if not stack:
                sol.append(0)
            else:
                sol.append(stack[-1] - i)
                
            stack.append(i)
            
        return sol[::-1]
