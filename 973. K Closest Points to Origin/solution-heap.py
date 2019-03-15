class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            d = x*x+y*y
            if len(heap) == K:
                heapq.heappushpop(heap, (-d, (x, y)))
            else:
                heapq.heappush(heap, (-d, (x, y)))
                
        return [p for d, p in heap]
