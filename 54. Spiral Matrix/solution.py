class Solution(object):
    # Initialise all the necessary variables for spiral
    def initialise(self, matrix):
        # Direction of spiral
        self.iDir = 0
        self.jDir = 1
        
        # Minimum and maximum limits for i and j 
        self.iLimit = {
            1: len(matrix) - 1,
            -1: 0
        }
        self.jLimit = {
            1: len(matrix[0]) - 1,
            -1: 0
        }
        
        # Total elements traversed
        self.totalElements = len(matrix) * len(matrix[0])
        
        # Transition of directions in clockwise direction
        self.transitionMap = {
            0: {
                1: [1, 0],
                -1: [-1, 0]
            },
            1: {
                0: [0, -1]
            },
            -1: {
                0: [0, 1]
            }
        }
            
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return matrix

        self.initialise(matrix)
        spiral = []
        i = 0
        j = 0
        count = 0
        while not count == self.totalElements:
            spiral.append(matrix[i][j])
            count += 1
            i, j = self.getPosition(i, j)
        return spiral

    # Get the next position in the spiral
    def getPosition(self, i, j):
        if self.iDir in [1, -1]:
            if i == self.iLimit[self.iDir]:
                self.iDir, self.jDir = self.transitionMap[self.iDir][self.jDir][0], self.transitionMap[self.iDir][self.jDir][1]
                return i, j + self.jDir
            else:
                return i + self.iDir, j

        if self.jDir in [1, -1]:
            if j == self.jLimit[self.jDir]:
                if -1 == self.jDir:
                    self.iLimit[1] = self.iLimit[1] - 1
                    self.iLimit[-1] = self.iLimit[-1] + 1
                    self.jLimit[1] = self.jLimit[1] - 1
                    self.jLimit[-1] = self.jLimit[-1] + 1
                self.iDir, self.jDir = self.transitionMap[self.iDir][self.jDir][0], self.transitionMap[self.iDir][self.jDir][1]
                return i + self.iDir, j
            else:
                return i, j + self.jDir
