class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # Time complexity - O(logN)
        # Space complexity - O(N)
        heapq.heappush(self.minHeap, num)
        if len(self.minHeap) > len(self.maxHeap):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)
            
        if self.minHeap and self.maxHeap and self.minHeap[0] < -self.maxHeap[0]:
            minNum = heapq.heappop(self.minHeap)
            maxNum = heapq.heappushpop(self.maxHeap, -minNum)
            heapq.heappush(self.minHeap, -maxNum)
            
    def findMedian(self) -> float:
        # Time complexity - O(1)
        # Space complexity - O(1)
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2.0
        else:
            return -1.0 * self.maxHeap[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
