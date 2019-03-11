class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # calculate frequency
        map = {}
        for t in tasks:
            if t in map:
                map[t] += 1
            else:
                map[t] = 1
                
        # create heap for freq
        heap = []
        for t, f in map.items():
            heapq.heappush(heap, -f)
            
        aux = []
        count = 0
        while heap:
            i = 0
            while i <= n and heap:
                f = heapq.heappop(heap)
                f += 1
                if f:
                    aux.append(f)
                i += 1
                
            if aux:
                count += n+1
            else:
                count += i
                
            while aux:
                heapq.heappush(heap, aux.pop())
            
        
        return count
