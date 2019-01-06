class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        sol = []
        for i, t in enumerate(T[::-1]):
            while stack and stack[-1][0] <= t:
                stack.pop()
            if stack:
                sol.append(i-stack[-1][1])
            else:
                sol.append(0)
            stack.append((t, i))
            
        sol.reverse()
        return sol
