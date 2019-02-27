class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) == k:
                if heap[0] < num:
                    heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
                
        return heap[0]
