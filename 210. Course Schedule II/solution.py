from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Create a mapping from prereq to course and vice versa
        prereqToCourse = defaultdict(lambda: set())
        courseToPrereq = defaultdict(lambda: set())
    
        for course, prereq in prerequisites:
            prereqToCourse[prereq].add(course)
            courseToPrereq[course].add(prereq)
            
        # Get a list of courses with prereqs taken - starting point
        prereqsTaken = [course for course in range(numCourses) if not courseToPrereq[course]]
        
        # Loop over and start taking courses 
        coursesTaken = []
        while prereqsTaken:
            prereqRecentlyTaken = []
            for prereq in prereqsTaken:
                coursesTaken.append(prereq)
                for course in prereqToCourse[prereq]:
                    courseToPrereq[course].remove(prereq)
                    if not courseToPrereq[course]:
                        prereqRecentlyTaken.append(course)
            prereqsTaken = prereqRecentlyTaken
                    
        # If all courses are taken then there is a possible solution
        if len(coursesTaken) == numCourses:
            return coursesTaken
        else:
            return []
            
            
