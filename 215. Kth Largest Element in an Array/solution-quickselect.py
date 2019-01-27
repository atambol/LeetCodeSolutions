class Solution:
    def findKthLargest(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # find n - Kth smallest element
        n = len(nums) - 1
        K = n - K + 1
        
        # quick select algorithm
        i = 0
        j = n
        
        while i <= j:
            k = i   # pivot element index
            pivot = nums[i]
            
            # parition the array
            for x in range(i+1, j+1):
                if nums[x] < pivot:
                    if x == k + 1:
                        nums[k] = nums[x]
                    else:
                        nums[k], nums[x] = nums[x], nums[k+1]
                    k = k + 1
            
            # put back the pivot
            nums[k] = pivot
            
            # check if the pivot is the n - Kth largest element. Readjust otherwise
            if k == K:
                return nums[k]
            elif k > K:
                j = k - 1
            else:
                i = k + 1
                
        return nums[i]
