class Solution:
    def __init__(self):
        self.graph = {}
        self.visited = []
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        # edge case
        if len(M) < 2:
            return len(M)
        
        # count friend circles
        count = 0
        self.visited = [False]*len(M)
        for i in range(len(M)):
            if not self.visited[i]:
                self.dfs(M, i)
                count += 1
                
        return count
        
    def dfs(self, M, i):
        if self.visited[i]:
            return 
        self.visited[i] = True
        for j in range(len(M[i])):
            if M[i][j] == 1:
                self.dfs(M, j)

                
