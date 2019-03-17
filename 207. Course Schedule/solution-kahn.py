class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algorithm for toplogical sort
        # create the graph and indegree count
        graph = {}
        indegree = {}
        
        for course in range(numCourses):
            graph[course] = set()
            indegree[course] = 0
            
        for course, prereq in prerequisites:
            graph[course].add(prereq)
            indegree[prereq] += 1
            
        # find all the vertices with 0 in-degree
        deq = collections.deque()
        for course in range(numCourses):
            if not indegree[course]:
                deq.append(course)
        
        # remove each zero in-degree vertex
        visited = [False]*numCourses
        while deq:
            # visit the vertex
            course = deq.popleft()
            visited[course] = True
            
            # check every neighbour of this vertex
            for prereq in graph[course]:
                indegree[prereq] -= 1
                if not indegree[prereq]:
                    deq.append(prereq)
                
        if visited.count(True) != numCourses:
            return False
        else:
            return True
        
        
    
