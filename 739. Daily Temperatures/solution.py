class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        hash = {}
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)-1, -1, -1): 
            while stack and stack[-1] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = hash[stack[-1]] - i
            # else:
            #     res[i] = 0
            hash[temperatures[i]] = i
            stack.append(temperatures[i])
            # print(i, stack, hash)
        return res
