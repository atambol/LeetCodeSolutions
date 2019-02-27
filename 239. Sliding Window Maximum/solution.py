class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # edge case
        if not nums:
            return []
        
        # create the first window
        deq = collections.deque()
        for i in range(k):
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
                
            deq.append(i)
            
        # maintain a solution for each window
        sol = []
        sol.append(nums[deq[0]])
        
        # process the remaining windows
        for i in range(k,len(nums)):
            while deq and i - deq[0] >= k:
                deq.popleft()
                
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
                
            deq.append(i)
            sol.append(nums[deq[0]])
            
        return sol
