class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        visited = [False]*len(M)
        # visit each person if it has not yet been visted
        for i in range(len(M)):
            if not visited[i]:
                count += 1
                # visit his friends
                self.dfs(M, i, visited)
        return count
                
    def dfs(self, M, i, visited):
        visited[i] = True
        for j in range(len(M)):
            # visit his friend's friend
            if M[i][j] == 1 and not visited[j]:
                self.dfs(M, j, visited)
