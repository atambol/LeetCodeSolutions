class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # edge case
        if n == 0:
            return len(tasks)
        
        # count the tasks
        count = {}
        for task in tasks:
            try:
                count[task] += 1
            except KeyError:
                count[task] = 1
        
        # create a min heap from the tasks and their counts
        heap = []
        for k, v in count.items():
            heapq.heappush(heap, (-v, k))
        
        # count the number of intervals involved
        intervals = 0
        while heap:
            aux = []
            i = 0
            
            # remove the elements from heap upto n times
            while i <= n and heap:
                v, k = heapq.heappop(heap)
                if v + 1 < 0:
                    aux.append((v+1, k))
                i += 1
                intervals += 1
            
            # update the intervals
            if not heap and aux:
                intervals += n - i + 1

            # readjust the heap
            for v, k in aux:
                heapq.heappush(heap, (v, k))

        return intervals
