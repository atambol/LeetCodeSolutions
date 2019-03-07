class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # heap to maintain K closest points
        heap = []
        for x, y in points:
            dist=x*x + y*y
            if len(heap) < K:
                heapq.heappush(heap, (-dist, (x, y)))
            elif len(heap) == K and abs(heap[0][0]) > dist:
                heapq.heappushpop(heap, (-dist, (x, y)))
                
        return [h[1] for h in heap]
