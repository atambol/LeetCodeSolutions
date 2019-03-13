class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sol = []
        
        # edge case
        if not nums:
            return sol
        
        # get the first window
        win = collections.deque()
        for i in range(k):
            while win and nums[i] > nums[win[-1]]:
                win.pop()
            win.append(i)
        sol.append(nums[win[0]])
        
        # get the rest of it
        for i in range(k, len(nums)):
            if win and abs(win[0] - i) >= k:
                win.popleft()
            while win and nums[i] > nums[win[-1]]:
                win.pop()
            win.append(i)
            sol.append(nums[win[0]])
            
        return sol
