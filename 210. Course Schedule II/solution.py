class Solution:
    def __init__(self):
        self.graph = {}
        self.visited = 2
        self.visiting = 1
        self.unvisited = 0
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create graph
        for i in range(numCourses):
            self.graph[i] = set()
            
        for c, p in prerequisites:
            self.graph[c].add(p)
            
        # dfs
        order = []
        status = [self.unvisited]*numCourses
        for i in range(numCourses):
            if status[i] == self.unvisited:
                sol = self.dfs(i, status)
                if not sol:
                    return sol
                order.extend(sol)
                
        return order
    
    def dfs(self, course, status):
        if status[course] == self.visiting:
            return []
        
        status[course] = self.visiting
        
        sol = []
        for prerequisite in self.graph[course]:
            if status[prerequisite] == self.visited:
                continue
                
            sub = self.dfs(prerequisite, status)
            if not sub:
                return sub
            sol.extend(sub)
            
        sol.append(course)
        status[course] = self.visited
        return sol
                
                
