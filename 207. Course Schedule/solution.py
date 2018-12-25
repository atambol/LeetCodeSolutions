class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # create graph
        graph = {}
        for p, q in prerequisites:
            if p in graph:
                graph[p].add(q)
            else:
                graph[p] = set([q])
            
        # dfs visits every branch
        # unvisited => visited[p] = 0
        # being visited => visited[p] = 1   (to detect cycle)
        # visited => visited[p] = 2         (optimisation to not visit again)
        def dfs(p):
            sol = True
            if p in graph:
                # being visited, so if encountered again there is a cycle
                visited[p] = 1
                for q in graph[p]:
                    if visited[q] == 1:
                        sol = False
                        break
                    else:
                        if not dfs(q):
                            sol = False
                            break
                # this path need not be visited again
                visited[p] = 2
            return sol
            
        
        # dfs over each course to check for a cycle
        visited = [0]*numCourses
        for course in graph:
            # only visit unvisited nodes
            if visited[course] == 0:
                if not dfs(course):
                    return False
        return True
