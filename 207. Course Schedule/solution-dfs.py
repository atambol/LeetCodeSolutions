class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses:
            return True
        
        # create a graph
        self.graph = {}
        self.status = [False]*numCourses
        self.unvisited = 0
        self.visiting = 1
        self.visited = 2
        
        for course in range(numCourses):
            self.graph[course] = set()
            
        for course, prereq in prerequisites:
            self.graph[course].add(prereq)
            
        # dfs
        for course in range(numCourses):
            if self.status[course] == self.unvisited:
                cycle = self.dfs(course)
                if cycle:
                    return False
                
        return True
                
    def dfs(self, course):
        if self.status[course] == self.visiting:
            return True
        
        if self.status[course] == self.visited:
            return False
        
        self.status[course] = self.visiting
        for prereq in self.graph[course]:
            cycle = self.dfs(prereq)
            if cycle:
                return cycle
            
        self.status[course] = self.visited
        return False
        
