class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's algorithm, O(V+E) space and time
        # create graph and note the in-degrees
        graph = {}
        indegree = {}
        for course in range(numCourses):
            graph[course] = set()
            indegree[course] = 0
            
        for course, prereq in prerequisites:
            graph[course].add(prereq)
            indegree[prereq] += 1
            
        # get all vertices with indegree of 0
        deq = collections.deque()
        for course in range(numCourses):
            if not indegree[course]:
                deq.append(course)
                
        # visit all the vertex in deq and create topological sort
        visited = [False]*numCourses
        sort = []
        while deq:
            # mark visited
            course = deq.popleft()
            sort.append(course)
            visited[course] = True
            
            # update indegree of prereqs and add to deq if indegree is 0
            for prereq in graph[course]:
                indegree[prereq] -= 1
                if not indegree[prereq]:
                    deq.append(prereq)
                    
        # check if any unvisited node left (implies cycle)
        if visited.count(True) != numCourses:
            return []
        else:
            sort.reverse()
            return sort
