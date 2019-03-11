class Solution:
    def __init__(self):
        self.graph = {}
        self.visited = 2
        self.visiting = 1
        self.unvisited = 0
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create graph
        for i in range(numCourses):
            self.graph[i] = set()
            
        for c, p in prerequisites:
            self.graph[c].add(p)
            
        # dfs
        status = [self.unvisited]*numCourses
        for i in range(numCourses):
            if status[i] == self.unvisited:
                cycle = self.dfs(i, status)
                if cycle:
                    return False
                
        return True
    
    def dfs(self, course, status):
        if status[course] == self.visiting:
            return True
        
        if status[course] == self.visited:
            return False
        
        status[course] = self.visiting
        
        for prerequisite in self.graph[course]:
            cycle = self.dfs(prerequisite, status)
            if cycle:
                return True
            
        status[course] = self.visited
        return False
                
                
