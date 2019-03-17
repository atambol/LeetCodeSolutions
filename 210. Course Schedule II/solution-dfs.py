class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS coloring method for topological sorting, O(V+E)
        self.graph = {}
        self.visited = 2
        self.visiting = 1
        self.unvisited = 0
        self.status = [self.unvisited]*numCourses
        
        # create graph
        for course in range(numCourses):
            self.graph[course] = set()
            
        for course, prereq in prerequisites:
            self.graph[course].add(prereq)
            
        # perform dfs on each unvisited vertex
        self.sort = collections.deque()
        for course in range(numCourses):
            if self.status[course] == self.unvisited:
                cycle = self.dfs(course)
                if cycle:
                    return []
                
        return list(self.sort)
                
    def dfs(self, course):
        # check status
        if self.status[course]== self.visiting:
            return True
        if self.status[course] == self.visited:
            return False
        self.status[course] = self.visiting
        
        # visit every prereq for this course
        for prereq in self.graph[course]:
            cycle = self.dfs(prereq)
            if cycle:
                return True
        
        self.sort.append(course)
        self.status[course] = self.visited
        return False
