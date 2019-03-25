class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph = {}
        self.deq = collections.deque()
        self.inDegree = {}
        
        for c in range(numCourses):
            self.graph[c] = set()
            self.inDegree[c] = 0
            
        for c, p in prerequisites:
            self.graph[c].add(p)
            self.inDegree[p] += 1
            
        for c, d in self.inDegree.items():
            if not d:
                self.deq.append(c)
                
        sort = []
        while self.deq:
            c = self.deq.popleft()
            sort.append(c)
            for p in self.graph[c]:
                self.inDegree[p] -= 1
                if not self.inDegree[p]:
                    self.deq.append(p)
                    
        if len(sort) != numCourses:
            return []
        else:
            sort.reverse()
            return sort
            
        
