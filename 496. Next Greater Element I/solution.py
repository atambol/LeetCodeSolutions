class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2set = {}
        for i, num in enumerate(nums2):
            nums2set[num] = i
        sol = []
        
        for num in nums1:
            sol.append(-1)
            for j in range(nums2set[num], len(nums2)):
                if nums2[j] > num:
                    sol[-1] = nums2[j]
                    break
                        
        return sol
