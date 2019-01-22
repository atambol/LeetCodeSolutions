class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(M)
        visited = [False]*m
        
        # count the friend circles
        for i in range(m):
            if not visited[i]:
                self.dfs(i, visited, M)
                count += 1
            
        return count
    
    def dfs(self, i, visited, M):
        visited[i] = True
        
        for j in range(len(M[i])):
            if M[i][j] and not visited[j]:
                self.dfs(j, visited, M)
