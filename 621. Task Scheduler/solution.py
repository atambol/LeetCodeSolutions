class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # calculate frequency
        f = {}
        for task in tasks:
            try:
                f[task] += 1
            except KeyError:
                f[task] = 1
                
        # create a heap
        heap = []
        for task, freq in f.items():
            heapq.heappush(heap, (-freq, task))
            
        # print(heap)
        # consume tasks
        count = 0
        while heap:
            aux = []
            i = 0
            
            # consume top priority tasks first
            while heap and i <= n:
                f, t = heapq.heappop(heap)
                if f + 1 < 0:
                    aux.append((f+1, t))
                i += 1
            
            if not aux:
                count += i
            else:
                count += n + 1
                
            # rearrange tasks from aux to heap
            for tup in aux:
                heapq.heappush(heap, tup)
                
        return count
                
            
                
            
            
