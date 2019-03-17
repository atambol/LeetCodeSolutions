class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sol = []
        
        # edge case
        if not nums1 or not nums2:
            return sol
        
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        
        # heap to store candidate tuples
        # tuple format (candidate-total, index i, index j)
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        
        # look for candidates until the k pairs are found or all candidates are exhausted
        while len(sol) < k and heap:
            # extract the tuple with least sum
            _, i, j = heapq.heappop(heap)
            sol.append([nums1[i], nums2[j]])
            
            # check for candidate pair one cell below
            if i + 1 < n1:
                if (i+1, j) in visited:
                    visited.remove((i+1, j))
                else:
                    visited.add((i+1, j))
                    heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                    
            # check for candidate pair one cell right
            if j + 1 < n2:
                if (i, j+1) in visited:
                    visited.remove((i, j+1))
                else:
                    visited.add((i, j+1))
                    heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                    
        # time complexity: O(k*log(n1+n2))
        # space complexity: O(n1*n2)
        return sol
