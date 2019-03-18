class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            flag = 0 if num < x else 1
            diff = abs(num-x)
            if len(heap) == k:
                if diff < abs(heap[0][0]):
                    heapq.heappushpop(heap, (-diff, flag, num))
            else:
                heapq.heappush(heap, (-diff, flag, num))
                
        nums = []
        for _, _, num in heap:
            nums.append(num)
            
        nums.sort()
        return nums
