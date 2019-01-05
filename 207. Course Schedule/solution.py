class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # create a graph
        graph = {}
        for c in range(numCourses):
            graph[c] = set()
            
        for c, p in prerequisites:
            graph[c].add(p)
                
        # dfs visits every branch
        # unvisited => visited[p] = 0
        # being visited => visited[p] = 1   (to detect cycle)
        # visited => visited[p] = 2         (optimisation to not visit again)
        def dfs(visited, course):
            if visited[course] == 1:
                # the course is being taken, cycle detected
                return False
            
            if visited[course] == 2:
                # the course has been taken
                return True
            
            # mark the course as being taken
            visited[course] = 1
            
            # take all its prereqs
            for prereq in graph[course]:
                canTake = dfs(visited, prereq)
                if not canTake:
                    return False
            
            # mark the course taken
            visited[course] = 2
            return True
        
        # go over each course and get its prereqs
        visited = [0]*numCourses
        for c in graph:
            if visited[c] == 0:
                sol = dfs(visited, c)
                if not sol:
                    return False
            
        return True
