class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # edge case
        if not nums or not k or k == 1:
            return nums
        
        # use a dequeue
        deq = collections.deque()
        deq.append(0)
        sol = []
        
        # run the logic for the first window
        for i in range(1, k):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
        sol.append(nums[deq[0]])
        
        # loop over each window and recalculate max num
        for i in range(k, len(nums)):
            # remove deq elements that are outside the window
            while deq and i - deq[0] >= k:
                deq.popleft()
            
            # remove deq elements that are smaller than nums[i]
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
                
            # store the newest index
            deq.append(i)
                    
            # append the largest element
            sol.append(nums[deq[0]])
        
        return sol
