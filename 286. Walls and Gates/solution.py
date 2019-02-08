class Solution:
    def wallsAndGates(self, rooms: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify rooms in-place instead.
        """
        # collect all points of source
        gates = []
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    gates.append((i, j))
                    
        # start bfs from gate
        for i, j in gates:
            self.bfs(i+1, j, rooms, 1)
            self.bfs(i-1, j, rooms, 1)
            self.bfs(i, j-1, rooms, 1)
            self.bfs(i, j+1, rooms, 1)
            
    def bfs(self, i, j, rooms, dist):
        if 0 <= i < len(rooms) and 0 <= j < len(rooms[i]) and rooms[i][j] > dist:
            rooms[i][j] = dist
            self.bfs(i-1, j, rooms, dist + 1)
            self.bfs(i+1, j, rooms, dist + 1)
            self.bfs(i, j+1, rooms, dist + 1)
            self.bfs(i, j-1, rooms, dist + 1)

            
