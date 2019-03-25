class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph= {}
        self.unvisited = 0
        self.visited = 2
        self.visiting = 1
        self.status = [False]*numCourses
        
        for c in range(numCourses):
            self.graph[c] = set()
            
        for c, p in prerequisites:
            self.graph[c].add(p)
            
        sol = []
        for c in range(numCourses):
            if self.status[c] == self.unvisited:
                s = self.dfs(c)
                if not s:
                    return []
                sol.extend(s)
                
        return sol
    
    def dfs(self, course):
        if self.status[course] == self.visiting:
            return []
        
        self.status[course] = self.visiting
        sol = []
        for p in self.graph[course]:
            if self.status[p] == self.visited:
                continue
                
            s = self.dfs(p)
            if not s:
                return s
            
            sol.extend(s)
        sol.append(course)
            
        self.status[course] = self.visited
        return sol
                
