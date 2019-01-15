class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # edge cases
        if not nums:
            return []
        
        if not k:   # if window size is 0, then every num is sol
            return nums
        
        # main flow
        deq = collections.deque()
        sol = []
        
        # store the index of num largest in the first window
        for i in range(k):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
                
            deq.append(i)
            
        # store the index of each num in next window
        for i in range(k, len(nums)):
            sol.append(nums[deq[0]])
            
            if deq[0] < i - k + 1:
                deq.popleft()
            
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i) 
        
        # the last window
        sol.append(nums[deq[0]])     
        
        return sol
