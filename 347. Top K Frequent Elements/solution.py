class Solution:
    def topKFrequent(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            try:
                freq[num] += 1
            except KeyError:
                freq[num] = 1
                
        heap = []
        for k, v in freq.items():
            heapq.heappush(heap, (-v, k))
            
        sol = [k for v, k in heapq.nsmallest(K, heap)]
        return sol
