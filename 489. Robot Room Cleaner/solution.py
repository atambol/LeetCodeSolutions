# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
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

class Solution(object):
    def __init__(self):
        self.visited = set()
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0)
        
    def dfs(self, robot, x, y):
        # clean
        robot.clean()
        
        # mark visited
        self.visited.add((x,y))
        
        # find immediate cells around in anti-clockwise direction
        # always orient the robot facing up after moving to a cell
        # check top
        if not (x,y+1) in self.visited and robot.move():
            self.dfs(robot, x, y+1)
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
        else:
            robot.turnLeft()
        
        # check left
        if not (x-1,y) in self.visited and robot.move():
            robot.turnRight()
            self.dfs(robot, x-1, y)
            robot.turnRight()
            robot.move()
            robot.turnRight()
        else:
            robot.turnLeft()
        
        # checkt down
        if not (x, y-1) in self.visited and robot.move():
            robot.turnRight()
            robot.turnRight()
            self.dfs(robot, x, y-1)
            robot.move()
            robot.turnRight()
        else:    
            robot.turnLeft()
        
        # check right
        if not (x+1, y) in self.visited and robot.move():
            robot.turnLeft()
            self.dfs(robot, x+1, y)
            robot.turnLeft()
            robot.move()
            robot.turnRight()
        else:
            robot.turnLeft()

        # robot is back to the same cell facing up
