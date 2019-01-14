class Solution:
    def __init__(self):
        self.courses = None
        self.graph = {}
        self.unvisited = 0
        self.visiting = 1
        self.visited = 2
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # create the graph
        for c in range(numCourses):
            self.graph[c] = set()
            
        for c, p in prerequisites:
            self.graph[c].add(p)

        # maintain visited status of courses
        self.courses = [self.unvisited] * numCourses
        
        # check for each course if there is a loop
        for c in range(numCourses):
            if self.courses[c] == self.unvisited:
                loop = self.dfs(c)
                if loop:
                    return False

        return True
    
    def dfs(self, c):
        if self.courses[c] == self.visiting:
            return True
        if self.courses[c] == self.visited:
            return False
        self.courses[c] = self.visiting
        
        for p in self.graph[c]:
            loop = self.dfs(p)
            if loop:
                return True
            
        self.courses[c] = self.visited
        return False
            
            
            
