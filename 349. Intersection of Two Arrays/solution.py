class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        sol = set()
        for n in nums1:
            if n in nums2:
                sol.add(n)
                
        return list(sol)
