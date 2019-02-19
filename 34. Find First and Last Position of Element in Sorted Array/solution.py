class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        return self.search(nums, target, 0, len(nums)-1)
        
    def search(self, nums, target, low, high):
        sol = [-1, -1]
        # base condition
        if low > high:
            return sol
        
        # only one element between the indices
        elif low == high:
            if nums[low] == target:
                sol[0] = low
                sol[1] = low
            return sol
        else:
            # calculate mid
            mid = (low+high)//2
            
            # if mid is the target, look both sides
            if nums[mid] == target:
                sol1 = self.search(nums, target, low, mid-1)
                sol2 = self.search(nums, target, mid+1, high)
                sol = [mid, mid]
                if sol1[0] != -1:
                    sol[0] = sol1[0]
                if sol2[1] != -1:
                    sol[1] = sol2[1]
                return sol
            
            # mid is less than target, look right
            elif nums[mid] < target:
                return self.search(nums, target, mid+1, high)
            
            # mid is greater than target, look left
            else:
                return self.search(nums, target, low, mid-1)
                    
