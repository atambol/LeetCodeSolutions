# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def __init__(self):
        # keep track of the movements with first position as origin
        self.x = 0
        self.y = 0
        self.visited = set()
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # check visited status
        if (self.x, self.y) in self.visited:
            return
        else:
            self.visited.add((self.x, self.y))
        
        # clean this cell
        robot.clean()

        # clean above
        if robot.move():
            self.y += 1
            self.cleanRoom(robot)
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
            self.y -= 1
        
        # clean left
        robot.turnLeft()
        if robot.move():
            self.x -= 1
            robot.turnRight()
            self.cleanRoom(robot)
            robot.turnRight()
            robot.move()
            robot.turnLeft()
            self.x += 1
        else:
            robot.turnRight()
        
        # clean below
        robot.turnLeft()
        robot.turnLeft()
        if robot.move():
            self.y -= 1
            robot.turnLeft()
            robot.turnLeft()
            self.cleanRoom(robot)
            robot.move()
            self.y += 1
        else:
            robot.turnRight()
            robot.turnRight()
            
        # clean right
        robot.turnRight()
        if robot.move():
            self.x += 1
            robot.turnLeft()
            self.cleanRoom(robot)
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            self.x -= 1
        else:
            robot.turnLeft()
