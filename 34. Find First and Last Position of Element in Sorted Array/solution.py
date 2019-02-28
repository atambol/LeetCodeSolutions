class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        sol = self.search(nums, target, 0, len(nums)-1)
        if not sol:
            return [-1, -1]
        else:
            if len(sol) == 1:
                return [sol[0], sol[0]]
            else:
                return sol
        
    def search(self, nums, target, low, high):
        if high - low == 0:
            if nums[low] == target:
                return [low]
            else:
                []
        if high - low <= 1:
            sol = []
            if nums[low] == target:
                sol.append(low)
            if nums[high] == target:
                sol.append(high)
            return sol
        
        sol = []
        mid = (low+high)//2
        if nums[mid] == target:
            sol.append(mid)
            sol.extend(self.search(nums, target, low, mid-1))
            sol.extend(self.search(nums, target, mid+1, high))
            return [min(sol), max(sol)]
        elif nums[mid] < target:
            return self.search(nums, target, mid+1, high)
        else:
            return self.search(nums, target, low, mid-1)

            
