class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2

            
        combined = []
        for i in range(l):
            if nums1 and nums2:
                m_min = min(nums1[0], nums2[0])
                combined.append(m_min)
                if nums1[0] == m_min:
                    nums1 = nums1[1:]
                else:
                    nums2 = nums2[1:]
                
            elif not nums1 and nums2:
                combined.extend(nums2)
                break
            else:
                combined.extend(nums1)
                break
                
        print(combined)
        print(int(l/2))
        if l % 2 == 0:
            return (combined[int(l/2-1)] + combined[int(l/2)])/2
        else:
            return combined[int(l/2)]
