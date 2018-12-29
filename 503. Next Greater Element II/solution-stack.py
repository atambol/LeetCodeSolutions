class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # use stack to store the largest element
        stack = []
        l = len(nums)
        sol = [-1]*l
        
        # first round
        for i in range(l-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                sol[i] = stack[-1]
            else:
                sol[i] = -1
            stack.append(nums[i])

        # second round since we use circular list
        for i in range(l-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                sol[i] = stack[-1]
            else:
                sol[i] = -1
            stack.append(nums[i])
            
        return sol
                
        
