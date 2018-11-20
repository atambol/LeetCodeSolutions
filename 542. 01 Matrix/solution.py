class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # construct the solution matrix
        l = len(matrix)
        sol = []
        for i in range(l):
            sol.append([])
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    sol[i].append(0)
                else:
                    sol[i].append(sys.maxsize)
        
        # look up starting from first position
        for i in range(l):
            for j in range(len(matrix[i])):
                dist = sol[i][j]
                if matrix[i][j] == 1:
                    if i - 1 >= 0:
                        if dist > sol[i-1][j] + 1:
                            dist = sol[i-1][j] + 1
                    if j - 1 >= 0:
                        if dist > sol[i][j-1] + 1:
                            dist = sol[i][j-1] + 1
                sol[i][j] = dist
                
                
        # look down this time starting from last position
        for i in range(l-1, -1, -1):
            for j in range(len(matrix[i])-1, -1, -1):
                dist = sol[i][j]
                if matrix[i][j] == 1:
                    if i + 1 < l:
                        if dist > sol[i+1][j] + 1:
                            dist = sol[i+1][j] + 1
                    if j + 1 < len(matrix[i]):
                        if dist > sol[i][j+1] + 1:
                            dist = sol[i][j+1] + 1
                sol[i][j] = dist
        
        return sol
