class Solution:
    def __init__(self):
        self.graph = {}
        self.unvisited = 0
        self.visiting = 1
        self.visited = 2
        self.status = None
        
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # create graph
        for c in range(numCourses):
            self.graph[c] = set()
            
        for c, p in prerequisites:
            self.graph[c].add(p)
            
        # perform dfs and get the order
        order = []
        self.status = [0]*numCourses
        
        for c in range(numCourses):
            if self.status[c] == self.unvisited:
                suborder = self.dfs(c)
                if not suborder:
                    return suborder
                order.extend(suborder)
        
        return order
    
    def dfs(self, course):
        # mark visiting
        self.status[course] = self.visiting
        order = []
        
        # find order for each preqreq of this course
        for prereq in self.graph[course]:
            # prereq cannot be taken with the course
            if self.status[prereq] == self.visiting:
                return []
            
            # add the order of prereq
            if self.status[prereq] == self.unvisited:
                suborder = self.dfs(prereq)
                if not suborder:
                    return []
                
                order.extend(suborder)
                
        # mark visited
        self.status[course] = self.visited        
        order.append(course)
        return order
            
