class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # create a graph for courses and prereqs
        graph = {}
        for c in range(numCourses):
            graph[c] = set()
            
        for c, p in prerequisites:
            graph[c].add(p)
            
        # dfs visits every branch
        # course not taken => visited[p] = 0
        # course being taken => visited[p] = 1   (to detect cycle)
        # course has been taken => visited[p] = 2   (optimisation to not take again)
        def dfs(visited, c):
            
            # only courses with visited[c] = 0 will be visited
            visited[c] = 1
            
            # final order of courses
            order = []
            
            # take every prerequisite
            for p in graph[c]:
                
                # if it is being taken, cycle is present
                if visited[p] == 1:
                    return []
                
                # if it has been taken, dont need to retake it
                if visited[p] == 2:
                    continue
                
                # get the prerequisite's course order
                prereq_order = dfs(visited, p)
                
                # if it is empty, there is not solution
                if not prereq_order:
                    return prereq_order
                
                # add prereq's order to courses order
                order.extend(prereq_order)
            
            # add the course to the order at the end
            order.append(c)
            
            # mark the course as taken
            visited[c] = 2
            
            return order
        
        # visit each course in graph
        visited = [0]*numCourses
        sol = []
        for c in graph:
            if visited[c] == 0:
                course_order = dfs(visited, c)
                if not course_order:
                    return course_order
                sol.extend(course_order)
                
        return sol
