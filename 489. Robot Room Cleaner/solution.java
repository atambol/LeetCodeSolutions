/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * interface Robot {
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     public boolean move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     public void turnLeft();
 *     public void turnRight();
 *
 *     // Clean the current cell.
 *     public void clean();
 * }
 */
class Solution {
    HashMap<Integer, HashSet<Integer>> visited = new HashMap<Integer, HashSet<Integer>>();
    
    public void cleanRoom(Robot robot) {
        cleanRoom(robot, 0 , 0);
    }
    
    public void cleanRoom(Robot robot, Integer i , Integer j) {
        if (visited.containsKey(i) && visited.get(i).contains(j)) {
            return;
        }
        
        HashSet<Integer> set;
        if (!visited.containsKey(i)) {
            set = new HashSet<Integer>();
            visited.put(i, set);
        } else {
            set = visited.get(i);
        }
        set.add(j);
        
        robot.clean();
        
        // left
        robot.turnLeft();
        if (robot.move()) {
            robot.turnRight();
            cleanRoom(robot, i-1, j);
            robot.turnRight();
            robot.move();
            robot.turnLeft();
        } else {
            robot.turnRight();
        }
        
        // down
        robot.turnLeft();
        robot.turnLeft();
        if (robot.move()) {
            robot.turnRight();
            robot.turnRight();
            cleanRoom(robot, i, j-1);
            robot.move();
        } else {
            robot.turnRight();
            robot.turnRight();
        }
        
        // right
        robot.turnRight();
        if (robot.move()) {
            robot.turnLeft();
            cleanRoom(robot, i+1, j);
            robot.turnLeft();
            robot.move();
            robot.turnRight();
        } else {
            robot.turnLeft();
        }
        
        // up
        if (robot.move()) {
            cleanRoom(robot, i, j+1);
            robot.turnLeft();
            robot.turnLeft();
            robot.move();
            robot.turnLeft();
            robot.turnLeft();
        }
    }
}
